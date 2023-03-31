import streamlit as st
from tflm_hello_world.training import train_model

st.set_page_config(
    page_title='Training',
    page_icon='✅',
    layout='wide'
)


def training_page():
    if "selected_dataset" not in st.session_state:
        st.error("No dataset was selected. Please select one on the Data page.")
        return

    if "selected_model" not in st.session_state:
        st.error("No model was selected. Please select one on the Model page.")
        return

    model_path = st.session_state.selected_model["Model Path"]
    train = train_model(st.session_state.selected_dataset, model_path) 
    st.title('Training')
    st.subheader('Train a Keras model')

    st.subheader("Model Training Settings")
    epochs = st.number_input("Enter the number of epochs", min_value=int(0))
    if epochs:
        batch_size = st.number_input("Enter the batch size", min_value=int(0))
        if batch_size:
            img_width = st.number_input("Enter image width", min_value=int(0))
            if img_width:
                img_height = st.number_input("Enter image height", min_value=int(0))
                if img_height:
                    train_ds, test_ds = train.load_data(img_height, img_width, batch_size)
                    if 'train_ds' not in st.session_state:
                        st.session_state.train_ds = train_ds
                    if train_ds and test_ds:
                        optim_choice = st.radio("Choose a loss function",("Some other loss function", "Sparse Categorical crossentropy"))
                        if optim_choice:
                            if st.button("Train"):
                                with st.spinner("Training..."):
                                    plot = st.empty()
                                    test = st.empty() 
                                    model, history, epochs_range = train.train(img_height, img_width, epochs, optim_choice, train_ds, test_ds)
                                st.success("Model trained successfully!")

                                data = train.plot_statistics(history, epochs_range)
                                tests, label = train.prediction(model, train_ds.class_names)
                                if 'model' not in st.session_state:
                                    st.session_state.model = model
                                plot.image(data)
                                test.image(tests, caption=label)
                                model.save(f"{model_path}/keras_model")
                                st.success("Model saved!")
training_page()
