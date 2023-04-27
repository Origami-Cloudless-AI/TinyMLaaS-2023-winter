import streamlit as st
import time
import requests
from tflm_hello_world.installing import ArduinoNano33BLE_Installer 
from tflm_hello_world.installing import ArducamPico4ML_Installer

# Dummy data
models = {
    "model1": {"accuracy": 0.9, "latency": 0.1},
    "model2": {"accuracy": 0.8, "latency": 0.2},
    "model3": {"accuracy": 0.7, "latency": 0.3},
}

devices = {
    "Arducam Pico4ML" : {"arch": "ARM", "cpu": "RP2040", "installer" : ArducamPico4ML_Installer(), "relay_id" : "RPI"},
    "Arduino Nano 33 BLE" : {"arch": "ARM", "cpu": "RP2040", "installer" : ArduinoNano33BLE_Installer(), "relay_id" : "Nano"},
}


def install_settings(selected_model, selected_device):
    st.header("Installation Settings")
    st.write(f"Selected Model: **{selected_model}**")
    st.write(f"Selected Device: **{selected_device}**")




def install_status(device):
    installer = device["installer"]
    if "selected_model" not in st.session_state:
        st.error("No model was selected. Please select one in the model tab")
        return
    generate_clicked = st.button("Generate")
    if generate_clicked:
        exists = False #False 

        st.header("Compilation Status")
        with st.spinner("Compiling  image..."):
            if exists == False: #Skip compiling for testing purposes to save time and just use the one in dockerhub
                installer.compile(st.session_state.selected_model["Model Path"])
                installer.upload()
            st.session_state["install_compile_done"] = True
            st.success("Compiling done! Uploaded to Dockerhub")

    if st.session_state.get("install_compile_done", False):
        if not "bridge" in st.session_state:
            st.error("No relay server selected. Select one in the device tab.")
        
        install_clicked = st.button("Install", disabled=(not "bridge" in st.session_state)) 
        if install_clicked:
            with st.spinner("Uploading..."):
                url = st.session_state.bridge+'/install'
                r = requests.post(url, json = {'device' : device["relay_id"]})
                st.success("Upload done!")

st.set_page_config(page_title="TinyML Install", page_icon=":rocket:")
st.title("TinyML Install")

selected_model = st.selectbox("Select Model", list(models.keys()))

selected_device = st.selectbox("Select Device", list(devices.keys()))

install_settings(selected_model, selected_device)

install_status(devices[selected_device])
