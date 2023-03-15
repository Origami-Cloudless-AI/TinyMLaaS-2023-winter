import streamlit as st
import time
from tflm_hello_world.installing import ArduinoNano33BLE_Installer 

# Dummy data
models = {
    "model1": {"accuracy": 0.9, "latency": 0.1},
    "model2": {"accuracy": 0.8, "latency": 0.2},
    "model3": {"accuracy": 0.7, "latency": 0.3},
}

devices = {
    "device1": {"arch": "x86", "cpu": "Intel Core i7"},
    "device2": {"arch": "ARM", "cpu": "Cortex-M4"},
    "device3": {"arch": "RISC-V", "cpu": "RV32IMC"},
}


def install_settings(selected_model, selected_device):
    st.header("Installation Settings")
    st.write(f"Selected Model: **{selected_model}**")
    st.write(f"Selected Device: **{selected_device}**")

def install_status():
    install_clicked = st.button("Generate")
    if install_clicked:
        st.header("Compilation Status")
        with st.spinner("Compiling OS image..."):
            ArduinoNano33BLE_Installer().compile()
            st.success("Compiling done!")

st.set_page_config(page_title="TinyML Install", page_icon=":rocket:")
st.title("TinyML Install")

selected_model = st.selectbox("Select Model", list(models.keys()))

selected_device = st.selectbox("Select Device", list(devices.keys()))

install_settings(selected_model, selected_device)

install_status()
