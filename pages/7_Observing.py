import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import altair as alt
from tflm_hello_world.observing import *

def observe_person_detection():
    "Shows UI for starting and stopping displaying the results of person detection"
    if "bridge" not in st.session_state:
        st.error("Relay server has not been selected. Select it on the device page.")
        return
    
    if "dataset_name" not in st.session_state:
        st.error("No dataset was selected. Please select one on the Data page.")
        return
    
    st.header("Person detection")
    bt_columns = st.columns(8)
    start_clicked = bt_columns[0].button("Start")

    prediction = st.empty()
    st.subheader('Device Output')

    prediction_df = pd.DataFrame(columns=['Time', 'Dataset', 'Device', 'Prediction Score'])
    if start_clicked:
        if not bt_columns[1].button("Stop"):
            error_label = st.empty()
            all_predictions = st.empty()
            while True:
                result = read_person_detection_from_relay(st.session_state.bridge, "/dev/ttyACM0")
                if not result:
                    error_label.error("Unable to read from device.")
                else:
                    score, time = result['Person'], datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    predictions_statics = pd.DataFrame({'Time': [time],
                                                        'Dataset': [st.session_state.dataset_name],
                                                        'Device': [st.session_state.device],
                                                        'Prediction Score':[score]})
                    
                    prediction_df = pd.concat([predictions_statics, prediction_df], ignore_index=True)
                    prediction.write(f"Person score: {score}%")
                    all_predictions.write(prediction_df)
    

st.set_page_config(page_title='Device Observing Dashboard',layout='wide')

observe_person_detection()
