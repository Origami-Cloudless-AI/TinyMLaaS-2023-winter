import streamlit as st
import pandas as pd
from tflm_hello_world.aws_s3 import s3_conn
import os
import numpy as np
from PIL import Image


def get_img_df(img_list):
    " Converts img list to pd.DataFrame "
    img_df = pd.DataFrame(columns=['File name', 'Label'])
    for img in img_list:
        row_to_append = pd.DataFrame([{'File name': img[2], 'Label':img[1]}])
        img_df = pd.concat([img_df, row_to_append], ignore_index=True)

    return img_df

def store_images(img_set, i, unlabeled=True, label_list=("Unlabeled", 0, 1)):
    " Stores a list of images to AWS S3"
    selected_imgs = []

    # If the image is in Unlabeled directory
    if unlabeled is True:
        label_list = (0, 1)
    
    for img in img_set:
        st.image(img)
        check = st.checkbox("Choose image", key=f"check_{i}")
        if check:
            label = st.radio("Select label", label_list, key=f"label_{i}")
            if unlabeled:
                selected_imgs.append([img, label, img.filename])            
            else:
                selected_imgs.append([img, label, img.name])
        i += 1

    if len(selected_imgs) > 0:
        st.write('You selected following images:')
        images_df = get_img_df(selected_imgs)
        st.dataframe(images_df)

        store_btn = st.button("Store images", key=f"button_{i}")
        if store_btn:
            for img in selected_imgs:
                if unlabeled:
                    s3_conn.move(dir_old='Unlabeled', dir_new=img[1], file_name=img[2])
                else:
                    s3_conn.upload_img(img[0], img[1], img[2])
            st.write("Images stored successfully!")
    else:
        st.write("You haven't chosen any image")

    return i

                
st.set_page_config(
    page_title='Data',
    page_icon='✅',
    layout='wide'
)

if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

col1, col2, col3 = st.columns([1, 2, 1])

col1.markdown(" # Upload data")


def change_photo_state():
    st.session_state["photo"] = "done"


dataset_names = []
dataset_locations = []
dataset_sizes = []
dataset_descriptions = []
file_images = []

name_column_name = "Dataset_Name"
url_column_name = "Location"
size_column_name = "Size"
description_column_name = "Description"

def upload_csv():
    df = pd.read_csv("dataset.csv")
    name_list = df[name_column_name]
    location_list = df[url_column_name]
    size_list = df[size_column_name]
    description_list = df[description_column_name]

    for name in name_list:
        dataset_names.append(name)
    for location in location_list:
        dataset_locations.append(location)
    for size in size_list:
        dataset_sizes.append(size)
    for description in description_list:
        dataset_descriptions.append(description)

def load_img(img):
    im = Image.open(img)
    image = np.array(im)
    return image

upload_csv()

with st.expander("Click to choose datasets"):
        for j in range(len(dataset_names)):
            st.write(dataset_names[j],dataset_sizes[j],dataset_descriptions[j])
            show = st.checkbox("Choose dataset", key=dataset_names[j])
            if show:
                st.session_state["photo"] = "done"
                for folder in os.listdir(dataset_locations[j]):
                    folderpath = dataset_locations[j]+folder
                    label = folder
                    for image in os.listdir(folderpath):
                        file = folderpath+"/"+image
                        img = load_img(file)
                        file_images.append(img)

uploaded_photo = col2.file_uploader(
    "Upload a photo", accept_multiple_files=True, on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

i = 0
if st.session_state["photo"] == "done":
    bar = col2.progress(0)
    for x in range(100):
        bar.progress(x+1)

    col2.success("Photo uploaded successfully")

    col3.metric(label="Temperature", value="-25℃ ", delta="3℃ ")
    st.header("Uploaded images")
    with st.expander("Click to see uploaded images"):
        if camera_photo:
            each = camera_photo
            st.image(each)
            st.checkbox("Choose image", key=i)
            i += 1

        if uploaded_photo:
            i = store_images(uploaded_photo, i, False)
            i += 1

        if len(file_images)>0:
            i = store_images(file_images, i, False)
            i += 1

st.header("Unlabeled images")
UNLABELED_DIR = "Unlabeled/"

with st.expander("Label unlabeled images"):
    unlabeled_count = s3_conn.count_objects(UNLABELED_DIR)
    if unlabeled_count == 0:
        st.text("All images are already labeled.")
    else:
        st.write(f"{unlabeled_count} unlabeled images found")
        unlabeled_imgs = s3_conn.read_images(UNLABELED_DIR)
        i = store_images(unlabeled_imgs, i, True)
        i += 1