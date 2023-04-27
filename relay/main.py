import subprocess
import getpass
from flask import Flask, abort, request, jsonify
#from pyngrok import ngrok
from tflm_hello_world.observing import read_person_detection_from_serial



app = Flask(__name__)
port = 5000


@app.route('/install', methods=['POST'])
def install():
    if request.method == 'POST':
        if "device" not in request.get_json():
            return "No device in request", 400
        device = request.get_json()["device"]
        
        upload_funcs = {
            "RPI" : upload_rpi, 
            "Nano" : upload
        }
        
        if device not in upload_funcs.keys():
            return f"Device \"{device}\" is not supported"

        upload_funcs[device]()
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


def upload():
    "Uploads compiled sketch in docker"
    #Add sudo if docker permission errors
    port = get_device_port("Nano")
    cmd = f"docker run --privileged ohtuprojtinymlaas/nano33ble upload -p {port} --fqbn arduino:mbed_nano:nano33ble template"
    subprocess.run([cmd], shell=True)


def upload_rpi():
    "Uploads compiled person detection uf2 file to device. The device must be in the USB Mass Storage Mode and `device_path` should be the absolute path at which the device is mounted at."
    device_path = f"/media/{getpass.getuser()}/RPI-RP2"
    docker_img = "ohtuprojtinymlaas/pico"
    # this mounts the device_path inside the container and copies the uf2 file from the container to device_path
    cmd = f"docker run --rm -v {device_path}:/opt/mount --entrypoint cp {docker_img} person_detection_screen_int8.uf2 /opt/mount/app.uf2"
    subprocess.run([cmd], shell=True)



def get_device_port(device_name:str):
    return "/dev/ttyACM0"


if __name__ == "__main__":
    app.run()

