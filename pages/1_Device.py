import streamlit as st
import pandas as pd
# Define the list of steps and their statuses

st.set_page_config(
    page_title = 'Device',
    page_icon = '✅',
    layout = 'wide'
)


st.title('Device')
st.header('Register a device')

new_device_name = st.text_input("Device name")
new_device_connection = st.text_input("Connection")
new_device_installer = st.text_input("Installer")
new_compiler = st.text_input("Compiler")
new_model = st.text_input("Model")
new_description = st.text_input("Description")

add_button = st.button("Add",key="add_button")
delete_button = st.button("Remove",key="delete_button")

df = pd.read_csv('TinyMLaaS.csv')

def warning(selected_devices):
    st.warning(selected_devices)

if delete_button:
    selected_devices = st.multiselect("Devices", options=df['Device name'].tolist(), key="selected_devices")

    df = df[~df["Device name"].isin(selected_devices)]
    df.to_csv("TinyMLaaS.csv", mode="w", index=False)


if add_button: 
    new_device_data = pd.DataFrame(
        {
        "Device name": [new_device_name],
        "Connection": [new_device_connection],
        "Compiler": [new_compiler],
        "Model": [new_model],
        "Description": [new_description]
        }
    )

    df = pd.DataFrame(new_device_data)

    df.to_csv('TinyMLaaS.csv',mode="a",index=False,header=False)
    st.info("Added new data")


df = pd.read_csv('TinyMLaaS.csv')

st.header('List all registered devices')
st.subheader('Filter devices with interactive table')
st.dataframe(df)

st.subheader('Device location')
st.markdown('https://streamlit-demo-uber-nyc-pickups-streamlit-app-456wus.streamlit.app/')

