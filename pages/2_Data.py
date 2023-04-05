import streamlit as st
import pandas as pd
from tflm_hello_world.aws_s3 import s3_conn
import os
from PIL import Image


def get_img_df(img_list):
    " Converts img list to pd.DataFrame "
    img_df = pd.DataFrame(columns=['File name', 'Label'])
    for img in img_list:
        row_to_append = pd.DataFrame([{'File name': img[2], 'Label':img[1]}])
        img_df = pd.concat([img_df, row_to_append], ignore_index=True)

    return img_df

def store_images(img_set, i, unlabeled=False, pil_img=False):
    " Stores a list of images to AWS S3"
    selected_imgs = []
    label_list=("Unlabeled", 0, 1)

    # If the image is in Unlabeled directory
    if unlabeled is True:
        label_list = (0, 1)
    
    for img in img_set:
        st.image(img)
        check = st.checkbox("Choose image", key=f"check_{i}")
        if check:
            label = st.radio("Select label", label_list, key=f"label_{i}")
            if pil_img:
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

def store_dataset(img_set):
    " Store a dataset to AWS S3"
    for img in img_set:
        s3_conn.upload_img(img, img.label, img.filename, True)
    st.write("Images stored successfully!")

def move_to_next_page(count_pages, current_page):
    if current_page < count_pages - 1:
        current_page += 1
        st.session_state["current_page"] = current_page
        st.experimental_rerun()

def move_to_previous_page(current_page):
    if current_page > 0:
        current_page -= 1
        st.session_state["current_page"] = current_page
        st.experimental_rerun()

def display_current_page(images, current_page):
    " Selects images for displaying"

    num_cols, images_per_page = 5, 50

    num_rows = len(images) // num_cols + (len(images) % num_cols > 0)

    with st.container():
        start_idx = current_page * images_per_page
        end_idx = min(start_idx + images_per_page, len(images))
        page_images = images[start_idx:end_idx]

        for j in range(num_rows):
            cols = st.columns(num_cols)
            for k in range(num_cols):
                index = j * num_cols + k
                if index < len(page_images):
                    cols[k].image(page_images[index], caption=f"{page_images[index].filename}")

def display_images(images):
    " Show max 50 images on each page in Data tab"

    images_per_page = 50

    count_pages = len(images) // images_per_page + (len(images) % images_per_page > 0)
    current_page = st.session_state.get("current_page", 0)

    button_container = st.container()

    prev_col, page_col, next_col = button_container.columns([1, 1, 1])

    if current_page > 0:
        if prev_col.button("Previous", key=f"Previous"):
            move_to_previous_page(current_page)

    with page_col:
        if count_pages != 0:
            st.write(f"{current_page + 1}/{count_pages}")

    if current_page < count_pages - 1:
        if next_col.button("Next", key=f"Next"):
            move_to_next_page(count_pages, current_page)

    display_current_page(images, current_page)

def update_stored_images():
    " Fetching images from AWS/Localstack for viewing or deleting"

    folders = ["Unlabeled", "0", "1"]

    selected_folder = st.selectbox('Choose a folder', folders)
    imgs = s3_conn.read_images(selected_folder)
    if len(imgs) > 0:
        if st.button(f"Remove images from {selected_folder}", key=f"remove_button_{i}"):
            s3_conn.remove_objects(selected_folder)
    
    display_images(imgs)
                
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

upload_csv()

def load_img(url):
    img = Image.open(url)
    return img

st.header("Available devices")
with st.expander("Click to choose devices"):
    st.write("Not working :DD")

st.header("Available datasets")
with st.expander("Click to choose datasets"):
        for j in range(len(dataset_names)):
            st.write(dataset_names[j],dataset_sizes[j],dataset_descriptions[j])
            show = st.checkbox("Choose dataset", key=dataset_names[j])
            if show:
                st.session_state["selected_dataset"] = dataset_locations[j]
                st.success(f"Selected {dataset_names[j]}") 
                st.session_state["photo"] = "done"
                for folder in os.listdir(dataset_locations[j]):
                    folderpath = dataset_locations[j]+folder
                    for image in os.listdir(folderpath):
                        file = folderpath+"/"+image
                        img = load_img(file)
                        img.filename = image
                        img.label = folder
                        file_images.append(img)
                store_btn = st.button("Store images", key=f"store_dataset")
                if store_btn:
                    store_dataset(file_images)

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
    if camera_photo:
        st.header("Uploaded camera images")
        with st.expander("Click to see camera photos"):
            each = camera_photo
            st.image(each)
            st.checkbox("Choose image", key=i)
            i += 1

    if uploaded_photo:
        st.header("Uploaded images")
        with st.expander("Click to see uploaded images"):
            i = store_images(uploaded_photo, i)
            i += 1

st.header("Label unlabeled images")
UNLABELED_DIR = "Unlabeled/"

with st.expander("Label unlabeled images"):
    unlabeled_count = s3_conn.count_objects(UNLABELED_DIR)
    if unlabeled_count == 0:
        st.text("All images are already labeled.")
    else:
        st.write(f"{unlabeled_count} unlabeled images found")
        unlabeled_imgs = s3_conn.read_images(UNLABELED_DIR)
        i = store_images(unlabeled_imgs, i, unlabeled=True, pil_img=True)
        i += 1

st.header("Stored images")
update_stored_images()
