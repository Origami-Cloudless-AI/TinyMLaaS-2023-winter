import subprocess
from flask import Flask, abort, request, jsonify
#from pyngrok import ngrok
from tflm_hello_world.observing import read_person_detection_from_serial



app = Flask(__name__)
port = 5000


@app.route('/install', methods=['POST'])
def install():
    if request.method == 'POST':
        print("Installing the compiled firmware")
        upload("/dev/ttyACM0")
        return 'Success', 200
    else:
        abort(400)


@app.route('/prediction', methods=['GET'])
def get_prediction():
    device = request.args.get("device", None)
    if not device:
        return "No device selected in request", 400
    port = get_device_port(device)
    pred = read_person_detection_from_serial(port)
    if not pred:
        return "Failed to read prediction from device", 404
    return jsonify(pred)


def upload(port:str):
    "Uploads compiled sketch in docker"
    #Add sudo if docker permission errors
    cmd = f"docker run --privileged ohtuprojtinymlaas/nano33ble upload -p {port} --fqbn arduino:mbed_nano:nano33ble template"
    subprocess.run([cmd], shell=True)


def get_device_port(device_name:str):
    return "/dev/ttyACM0"


if __name__ == "__main__":
    app.run()

