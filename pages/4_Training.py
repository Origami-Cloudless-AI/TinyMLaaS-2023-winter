import streamlit as st
from io import BytesIO
import matplotlib.pyplot as plt

from tflm_hello_world.training import model_training

st.set_page_config(
    page_title = 'Training',
    page_icon = '✅',
    layout = 'wide'
)

if "train" not in st.session_state:
    st.session_state["train"]="not done"

def change_train_state():
    st.session_state["train"] = "done"

class model_training_vis():
    def __init__(self):
        self.plot = st.empty()
        self.data = st.empty()
        self.test = st.empty()

    def render(self, history, epochs_range, model):
        data = trainer.plot_statistics(history, epochs_range)
        tests, label = trainer.prediction(model)
        
        self.plot.image(data)
        self.test.image(tests, caption=label)

trainer = model_training()
visual = model_training_vis()

st.title('Training')

st.subheader('Training a model')
download = st.button('Train the model', on_click=change_train_state)

if st.session_state["train"] == "done":
    status = st.text('Training the model...')
    model, history,epochs_range = trainer.train_model(img_height=180, img_width=180, batch_size=32)
    status.text('Model trained!')
    visual.render(history, epochs_range, model)
