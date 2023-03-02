import streamlit as st
import pandas as pd
from PIL import Image
from pages.aws_s3 import s3_conn


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

        store_btn = st.button("Store images")
        if store_btn:
            for img in selected_imgs:
                if unlabeled:
                    s3_conn.move(dir_old='Unlabeled', dir_new=img[1], file_name=img[2])
                else:
                    s3_conn.upload_img(img[0], img[1], img[2])
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
file_images = []
url_column_name = "change to the name of the column with url listing"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    url_list = df[url_column_name]
    for url in url_list:
        file_images.append(url)

uploaded_photo = col2.file_uploader("Upload a photo", accept_multiple_files=True, on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

i = 0
if st.session_state["photo"] == "done":
    bar = col2.progress(0)
    for x in range(100):
        bar.progress(x+1)

    col2.success("Photo uploaded successfully")

    col3.metric(label="Temperature", value="-25℃ ", delta="3℃ ")

    with st.expander("Click to read more"):
        st.write("Please complete this data acqusition feature")
        if camera_photo:
            each = camera_photo
            st.image(each)
            st.checkbox("Choose image", key=i)
            i += 1

        if uploaded_photo:
            store_images(uploaded_photo, i, False)
            i += 1

        if uploaded_file:
            for each in file_images:
                st.image(each)
                st.checkbox("Choose image", key=i)
                i += 1

st.header("Unlabeled images")
UNLABELED_DIR = "Unlabeled/"

unlabeled_count = s3_conn.count_objects(UNLABELED_DIR)
if unlabeled_count == 0:
    st.text("All images are already labeled.")
else:
    st.write(f"{unlabeled_count} unlabeled images found")
    unlabeled_imgs = s3_conn.read_images(UNLABELED_DIR)
    store_images(unlabeled_imgs, i, True)


