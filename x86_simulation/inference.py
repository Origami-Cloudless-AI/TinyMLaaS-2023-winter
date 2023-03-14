import tensorflow as tf
import cv2
import numpy as np
import os
import sys

def main():
    img_path = os.environ['image_path']
    model_path = os.environ['model_path']
    print("MODEL_PATH: ", model_path)
    interpreter = init_interpreter(model_path)

    classify(interpreter, img_path)

def classify(interpreter, path ):
    """Classify images passed to the function
    Returns:
        string: formatted string containing the results of the inference and time it took
    """

    image = tf.keras.utils.load_img(path, target_size=(180,180))
    img = tf.keras.utils.img_to_array(image)
    img = tf.expand_dims(img,0) #Create a Batch of 1

    predictions_lite = interpreter(rescaling_input=img)['dense_1']
    score_lite = tf.nn.softmax(predictions_lite)

    classes = {1 : "Human",
                0 : "Not-Human"}
    
    print("This image most likely belongs to {} with {} percent confidence.".format((classes[np.argmax(score_lite)]), (100 * np.max(score_lite))))

def init_interpreter(path):
    """_summary_

    Args:
        path (_string_): Path to the model .tflite
    Returns:
        _tflite interpreter_: returns the interpreter for inference
    """

    interpreter = tf.lite.Interpreter(model_path=path)
    interpreter.get_signature_list()
    classify_lite = interpreter.get_signature_runner('serving_default')

    return classify_lite

if __name__ == "__main__":
    main()
