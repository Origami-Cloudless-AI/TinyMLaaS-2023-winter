import subprocess
import streamlit as st
import time

from tflm_hello_world.compiling import convert_model, convert_to_c_array, plot_size, convert_model_to_cc


# Define some dummy data
models = {
    "Model 1": {
        "Accuracy": "80%",
        "Latency": "100ms",
        "Power Consumption": "10W"
    },
    "Model 2": {
        "Accuracy": "90%",
        "Latency": "50ms",
        "Power Consumption": "5W"
    },
    "Model 3": {
        "Accuracy": "95%",
        "Latency": "20ms",
        "Power Consumption": "3W"
    }
}


def compilation_tab():
    if "selected_model" not in st.session_state:
        st.error("No model was selected. Please select one in the model tab")
        return
    model_path = st.session_state.selected_model["Model Path"] 
    # Define the compilation settings tab
    st.subheader("Compilation Settings")
    quant = st.selectbox("Quantization", ["no quantization", "quantization", "end-to-end 8bit quantization"])
    if quant:
        generate = st.selectbox("Generate C array model", ["Yes", "No"])
        if generate:
            if "model" not in st.session_state:
                st.error("No trained model. Train one on the Training page.")
                return
            start = st.button("Compile")
            if start:
                with st.spinner("Compiling..."):
                    convert_model(st.session_state.train_ds, model_path, st.session_state.model)
                    if generate == "Yes":
                        convert_model_to_cc(model_path)
                st.write("Compilation complete!")
                plot = st.empty()
                plot.write(plot_size(model_path))


# Define the main function that runs the Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title="ML Compilation",layout="wide")



    # Define the sidebar options
    st.sidebar.title("Options")
    model_name = st.sidebar.selectbox("Select a model", list(models.keys()))

    # Define the main content area
    st.title("ML Compilation")
    st.header(f"Model: {model_name}")

    compilation_tab()

    # Define the model validation tab
    st.subheader("Model Validation")
    #Load model
    #loss, acc = model.validate() etc.etc.
    test = st.button("Test the model using x86 simulation")
    if test:
        subprocess.run(['Docker run '], shell=True)

    # Allow users to compare models
    st.subheader("Compare Models")
    model_names = list(models.keys())
    model_names.remove(model_name)
    compare_model_name = st.selectbox("Select a model to compare", model_names)
    st.write(f"Comparing {model_name} with {compare_model_name}")

    # Define the model packaging tab
    st.subheader("Model Packaging")
    st.selectbox("Select the target architecture", ["x86", "Arm", "nRF52840(Arduino Nano)"])

    # Define the packaging status tab
    with st.expander("Packaging Status"):
        # Simulate the packaging process with a progress bar
        with st.spinner("Packaging..."):
            for i in range(100):
                time.sleep(0.05)
                st.progress(i + 1)
        st.write("Packaging complete!")

# Run the app
if __name__ == "__main__":
    main()
