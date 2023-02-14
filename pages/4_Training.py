import streamlit as st
from io import BytesIO
import matplotlib.pyplot as plt

from tflm_hello_world.training import model_training

st.set_page_config(
    page_title = 'Training',
    page_icon = '✅',
    layout = 'wide'
)

class model_training_vis():
    def __init__(self):
        self.plot = st.empty()
        self.data = st.empty()
        self.test = st.empty()

    def render(self, history, epochs_range, model):
        data = trainer.plot_statistics(history, epochs_range)
        tests, label = trainer.prediction(model)
        fig = trainer.plot_size()
        
        self.plot.image(data)
        self.data.write(fig)
        self.test.image(tests, caption=label)

trainer = model_training()
visual = model_training_vis()

st.title('Training')

st.subheader('Training a model')
download = st.button('Train the model')

if download:
    status = st.text('Training the model...')
    model, history,epochs_range = trainer.train_model(img_height=180, img_width=180, batch_size=32)
    status.text('Model trained!')
    visual.render(history, epochs_range, model)
    trainer.convert_to_c_array()
