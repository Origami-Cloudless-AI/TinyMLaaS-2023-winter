import streamlit as st
import time

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

col1, col2, col3 = st.columns([1,2,1])

col1.markdown(" # Upload data")

def change_photo_state():
    st.session_state["photo"]="done"

uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":
   bar = col2.progress(0)
   for x in range(100):
       time.sleep(0.05)
       bar.progress(x+1)
   
   col2.success("Photo uploaded successfully")
   
   col3.metric(label="Temperature", value="-25℃ ", delta="3℃ ")
   
   with st.expander("Click to read more"):
       st.write("Please complete this data acqusition feature")
   
       if uploaded_photo is None:
           st.image(camera_photo)
       else:
           st.image(uploaded_photo)
           
