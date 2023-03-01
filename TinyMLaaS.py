import socket

import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title = 'TinyML as-a-Service',
    page_icon = '✅',
    layout = 'wide'
)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


def read_data_socket(sock_conn):
    
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            #st.success('Connected by',addr)
            return sock_conn.text('Connection success')
            #Handle incoming data here?
            #while True:
               # data = conn.recv(1024)
               # if not data: break
               # conn.sendall(data)

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def tinymlaas_page():
    st.title('TinyML as-a-Service')
    sock_conn = st.text('Socket status unknown')

    alerts = [
        {
        "device_name": "Temp",
        "alert_type": "low battery",
        "alert_mes": "Battery is at 10%"
        }
    ]
    read_data_socket(sock_conn)
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text('Done! (using st.cache)')

    with st.expander("Click to read more"):
        st.subheader('Raw data')
        st.write(data)

        st.subheader('Number of pickups by hour')
        hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))
        st.bar_chart(hist_values)

    st.subheader('Map of all pickups')
    st.map(data)

    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

tinymlaas_page()

