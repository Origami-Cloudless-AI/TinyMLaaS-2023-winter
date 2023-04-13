import subprocess
from flask import Flask, abort, request
from pyngrok import ngrok


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



def upload(port:str):
    "Uploads compiled sketch in docker"
    #Add sudo if docker permission errors
    cmd = f"docker run --privileged arskale/tinyml:nano33ble upload -p {port} --fqbn arduino:mbed_nano:nano33ble template"
    subprocess.run([cmd], shell=True)




if __name__ == "__main__":
    app.run()