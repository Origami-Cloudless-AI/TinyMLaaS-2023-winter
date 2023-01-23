import streamlit as st

st.set_page_config(
    page_title = 'Installing',
    page_icon = '✅',
    layout = 'wide'
)


st.title('Installing')
st.header('Installing Hello World binary in Container')
st.subheader('Build a container with a new hello world binary')
st.markdown('- List up devices')
st.markdown('- Choose a device')
st.markdown('- List up OS images')
st.markdown('- Choose an OS image')
st.markdown('- List up installers')
st.markdown('- Choose an installer')
st.markdown('- Confirm compatibility among device, OS image & installer')
st.markdown('- Start installation')
st.markdown('- Show the progress bar')
st.markdown('- Show the result OK / NG')
