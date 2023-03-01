import streamlit as st
import pandas as pd
import boto3
import os
import time
import requests
import tarfile


def get_img_df(img_list):
    " Converts img list to pd.DataFrame "
    img_df = pd.DataFrame(columns=['File name', 'Label'])
    for img in img_list:
        row_to_append = pd.DataFrame([{'File name': img[2], 'Label':img[1]}])
        img_df = pd.concat([img_df, row_to_append], ignore_index=True)

    return img_df

def store_s3(img_set, i):
    " Store list of images to AWS S3"
    s3 = boto3.client('s3')
    selected_imgs = []
    
    for img in img_set:
        st.image(img)
        check = st.checkbox("Choose image", key=i)
        if check:
            label = st.radio("Select label", (0, 1), key=f"label_{i}")
            selected_imgs.append([img, label, img.name])
        i += 1

    if len(selected_imgs) > 0:
        st.write('You selected following images:')
        images_df = get_img_df(selected_imgs)
        st.dataframe(images_df)

        store_btn = st.button("Store images")
        if store_btn:
            for img in selected_imgs:
                s3.upload_fileobj(img[0], f'tflmhelloworldbucket', f'{img[1]}/{img[0].name}')
            st.write("Images stored successfully!")
    else:
        st.write("You haven't chosen any image")

st.set_page_config(
    page_title = 'Data',
    page_icon = '✅',
    layout = 'wide'
)

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

col1, col2, col3 = st.columns([1,2,1])

col1.markdown(" # Upload data")

def change_photo_state():
    st.session_state["photo"]="done"

uploaded_file = col2.file_uploader("Choose a CSV file", on_change=change_photo_state)

dataset_names = []
dataset_locations = []
dataset_sizes = []
dataset_descriptions = []

name_column_name = "Dataset_Name"
url_column_name = "Location"
size_column_name = "Size"
description_column_name = "Description"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
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

    with st.expander("Click to choose datasets"):
        for j in range(len(dataset_names)):
            st.write(dataset_names[j],", ",dataset_locations[j],", ",dataset_sizes[j],", ",dataset_descriptions[j])
            show = st.checkbox("Choose dataset", key=dataset_names[j])
            if show:
                url = dataset_locations[j] # https://jovian.com/outlink?url=https%3A%2F%2Fs3.amazonaws.com%2Ffast-ai-imageclas%2Fstanford-cars.tgz
                target_path = 'temp/Common_brimstone_butterfly_(Gonepteryx_rhamni)_male_in_flight.jpg'
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open(target_path, "wb") as f:
                        f.write(r.content)
                        st.write("Saving file from url done")
                    with tarfile.open('cars/stanford-cars.tgz', 'r:gz' )as tar:
                        tar.extractall(path= 'cars/cars_data')
                    folderpath = 'cars/cars_data/stanford-cars/cars_train/'
                    for image in os.listdir(folderpath):
                        file = folderpath+"/"+image
                        with open(file, "rb") as f:
                            st.image(f.read(), width=200)
                            st.checkbox("Choose image", key=file)

uploaded_photo = col2.file_uploader("Upload a photo", accept_multiple_files=True, on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    bar = col2.progress(0)
    for x in range(100):
        bar.progress(x+1)

    col2.success("Photo uploaded successfully")

    col3.metric(label="Temperature", value="-25℃ ", delta="3℃ ")

    with st.expander("Click to read more"):
        st.write("Please complete this data acqusition feature")
        i = 0
        if camera_photo:
            each = camera_photo
            st.image(each)
            st.checkbox("Choose image", key=i)
            i += 1

        if uploaded_photo:
            store_s3(uploaded_photo, i)
            i += 1

st.header("Unlabeled images")

DATASET = "data/"
UNLABELED_DIR = "unlabeled/"
labels = ["None"]
for each in os.listdir(DATASET):
    labels.append(each)

for unlabeled_img in os.listdir(UNLABELED_DIR):
        filepath = UNLABELED_DIR+unlabeled_img
        with open(filepath, "rb") as f:
            columns = st.columns(5, gap="small")
            columns[0].image(f.read(), width=200)
            selected_label = columns[1].selectbox("Label:", labels, index=0, key=filepath)
            if selected_label != "None":
                os.rename(filepath, DATASET+selected_label+"/"+unlabeled_img)
                st.experimental_rerun()

if len(os.listdir(UNLABELED_DIR))==0:
    st.text("All images are already labeled.")

