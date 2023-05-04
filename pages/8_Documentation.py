import streamlit as st

# Set page configuration
st.set_page_config(
    page_title='Documentation',
    page_icon='✅',
    layout='wide'
)

# Add page title and subheader
st.title("Documentation")
st.subheader("Welcome to TinyML as a Service Application!")

# Create a dropdown menu for step selection
step_options = ["Select a step", "Device", "Data", "Model", "Training", "Compiling", "Installing", "Observing"]
selected_step = st.selectbox("Select a step to view", step_options)

# Display the selected step
if selected_step == "Device":
    st.header("Device")
    st.write("On the Device page, you can register a new device by plugging it into your computer's USB port and filling out the device information form. Once registered, you can check whether the device was successfully added by clicking the Refresh button.")
elif selected_step == "Data":
    st.header("Data")
    st.write("On the Data page, choose a dataset and click Store Images. Once the dataset is downloaded, you can view the images by selecting a folder.")
elif selected_step == "Model":
    st.header("Model")
    st.write("On the Model page, select a machine learning model to use for training.")
elif selected_step == "Training":
    st.header("Training")
    st.write("On the Training page, enter the number of training epochs and batch size, as well as the image width and height. Then click the Train button to begin training the model. You can view training and validation graphs once training is complete.")
elif selected_step == "Compiling":
    st.header("Compiling")
    st.write("On the Compiling page, click the Compile button to compile the trained model.")
elif selected_step == "Installing":
    st.header("Installing")
    st.write("On the Installing page, click the Generate button to install the compiled model on your device.")
elif selected_step == "Observing":
    st.header("Observing")
    st.write("On the Observing page, you can view image recognition predictions by clicking the Start button under Person Detection.")
else:
    st.write("Please select a step to view from the dropdown menu.")    
