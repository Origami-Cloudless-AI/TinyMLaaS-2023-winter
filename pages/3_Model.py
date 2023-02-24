import streamlit as st
import pandas as pd
import cv2
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import load_model


st.set_page_config(
        page_title = 'Model',
        page_icon = '✅',
        layout = 'wide'
    )


def save_selections():
    st.info("Your selections have been saved",icon="✅")

def visualize(model_meta):
    try:
        path = '/app/models/keras_model.h5'
        model = load_model(path)
        plot_model(model, to_file="/app/models/model.png", show_shapes=True)
        image = cv2.imread("/app/models/model.png")
        st.image(image)
    except:
        st.error("No model found")

def create_default_page():
    st.title("Model")
    
    models_df = read_file_with_models()
    print(models_df)
    #Display the models? 
    col1, col2, col3= st.columns(3)
    category = col1.radio('Select a category: ', models_df['Models'].keys())

    if category:
        models = models_df['Models'][category]
        select_model = col2.radio("Select a model:",list(models.keys()))
        
        if select_model:
            st.markdown(f" You have selected: **{select_model}** submodel under **{category}** model")
            
            table = "| Field | Description |\n| --- | --- | \n"
            for key,item in models[select_model].items():
                
                table += f"| {key} | {item} \n"
            
            
            st.markdown(table)
    
    col3.button("Select", on_click=save_selections)
    col3.button("Visualize", on_click=visualize, kwargs={'model_meta':models[select_model]})


  
def read_file_with_models():
    "Reads csv file that has the models and sets it to pandas dataframe "
    models_df = pd.read_json('pages/models.json')
    return models_df


create_default_page()