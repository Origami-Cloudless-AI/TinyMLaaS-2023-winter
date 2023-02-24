import streamlit as st

from tflm_hello_world.training import model_training

st.set_page_config(
    page_title = 'Compiling',
    page_icon = '✅',
    layout = 'wide'
)

if "compile" not in st.session_state:
    st.session_state["compile"]="not done"

st.title('Compiling')
st.header('Compiling Hello World TinyML model')
st.subheader('with TFLm tool')
st.markdown('- Choose compilation options')
st.markdown('- Compile into a deployable Docker image')
st.markdown('- Show the result')


def change_compile_state():
    st.session_state["compile"]="done"

st.button("Compile!", on_click=change_compile_state)
info = st.text("Status: waiting...")

if st.session_state["compile"] == "done":
    trainer = model_training()
    trainer.convert_to_c_array()
    info.text("Compilation successful!")


