import streamlit as st
import pandas as pd
# Define the list of steps and their statuses
import usb.core
import usb.util

st.set_page_config(
    page_title='Device',
    page_icon='✅',
    layout='wide'
)

state = st.session_state

def get_id_max():
    df = pd.read_csv("TinyMLaaS.csv")
    return df["id"].astype(int).max() + 1


def add():
    new_device_data = {
        "id": [get_id_max()],
        "Device name": [state.device_name],
        "Connection": [state.connection],
        "Installer": [state.installer],
        "Compiler": [state.compiler],
        "Model": [state.model],
        "Description": [state.description]
    }
    df = pd.DataFrame(new_device_data)
    with open("TinyMLaaS.csv", "a") as f:
        f.write("\n")
    df.to_csv("TinyMLaaS.csv", mode="a", header=False, index=False)
    st.info("Added new data")


def delete(df, id):
    df = df[~df['id'].isin([id])]
    df.to_csv("TinyMLaaS.csv", mode="w", index=False)
    st.success(f"Device #{id} removed.")


def modify(df, id):
    df = df[~df['id'].isin([id])]
    new_device_data = {
        "id": [id],
        "Device name": [state.device_name],
        "Connection": [state.connection],
        "Installer": [state.installer],
        "Compiler": [state.compiler],
        "Model": [state.model],
        "Description": [state.description]
    }
    df_modified = pd.DataFrame(new_device_data)
    df = pd.concat([df, df_modified], ignore_index=True)
    df.to_csv("TinyMLaaS.csv", mode="w", index=False)
    st.warning(f"Device #{id} modified")


def handle_add(manufacturer="", product="", serial=""):
    with st.form("new_device"):
        st.write("Add a new device")
        st.text_input("Device name", key="device_name",value=manufacturer)
        st.text_input("Connection", key="connection")
        st.text_input("Installer", key="installer")
        st.text_input("Compiler", key="compiler")
        st.text_input("Model", key="model", value=product)
        st.text_input("Description", key="description")

        submit = st.form_submit_button(label='Add', on_click=add)


def handle_modify(df, id, name, connection, installer, compiler, model, description):
    with st.form("modify_device"):
        st.write("Modify a device")
        st.text_input("Device name", value=name, key="device_name")
        st.text_input("Connection", value=connection, key="connection")
        st.text_input("Installer", value=installer, key="installer")
        st.text_input("Compiler", value=compiler, key="compiler")
        st.text_input("Model", value=model, key="model")
        st.text_input("Description", value=description, key="description")

        st.form_submit_button("Cancel")
        st.form_submit_button(
            "Modify Device", on_click=modify, args=(df, id,))


def handle_select(id, name, connection, installer, compiler, model, description):
    "Stores data of selected device to session state for other pages to use"
    device_data = {
        "id": id,
        "Device name": name,
        "Connection": connection,
        "Installer": installer,
        "Compiler": compiler,
        "Model": model,
        "Description": description 
    }
    state.selected_device = device_data
    st.success(f"Selected device: **{name}**")


def list_devices():
    st.header('All registered devices')
    df = pd.read_csv('TinyMLaaS.csv')
    # Device name, Connection, Installer, Compiler, Model, Description
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    for row in df.sort_values("id").itertuples():
        index, id, name, connection, installer, compiler, model, description = row
        col = st.columns(10)
        col[0].write(id)
        if "selected_device" in state and state.selected_device["id"] == id: # make selected device name bold
            col[1].write("**"+name+"**")
        else:
            col[1].write(name)
        col[2].write(connection)
        col[3].write(installer)
        col[4].write(compiler)
        col[5].write(model)
        col[6].write(description)
        col[7].button("Delete", key=name, on_click=delete, args=(df, id))
        col[8].button("Modify", key=f'm_{name}', on_click=handle_modify, args=(
            df, id, name, connection, installer, compiler, model, description))
        col[9].button("Select", key=f"s_{name}", on_click=handle_select, args=(
            id, name, connection, installer, compiler, model, description))

def list_connected_devices():
    st.header("All connected devices")

    #List all connected devices
    all_devices = usb.core.find(find_all=True)

    col1,col2,col3,col4 = st.columns(4)

    no_devices_found = True
    
    for device in all_devices:
        #Try / Except if any error occurs
        try:
            manufacturer = usb.util.get_string(device, device.iManufacturer)
            product = usb.util.get_string(device, device.iProduct)
            serial = usb.util.get_string(device, device.iSerialNumber)

            if manufacturer is not None:
                col1.write(manufacturer)
                col2.write(product)
                col3.write(serial)
                no_devices_found = False
                col4.button("register this device", key="2", on_click=handle_add,args=(manufacturer, product, serial))
        except:
            #Placeholder
            continue
    
    if no_devices_found:
        st.info("There is no connected devices currently!")
        



def device_locations():
    st.subheader('Device location')
    st.markdown(
        'https://streamlit-demo-uber-nyc-pickups-streamlit-app-456wus.streamlit.app/')

def device_page():
    st.title('Device')
    st.header('Register a device')

    st.button("register a new device", key="add_button", on_click=handle_add)

    list_connected_devices()
    list_devices()
    device_locations()


device_page()
