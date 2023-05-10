import subprocess
import getpass

DOCKERHUB_USER = "ohtuprojtinymlaas"


def install_inference(device_name : str):
    upload_funcs = {
        "RPI" : upload_rpi, 
        "Nano" : upload
    }
    if device_name not in upload_funcs.keys():
        return False
    upload_funcs[device_name]()
    return True


def upload():
    "Uploads compiled sketch in docker"
    #Add sudo if docker permission errors
    port = get_device_port("Nano")
    image = f"{DOCKERHUB_USER}/nano33ble"
    subprocess.run([f"docker pull {image}"], shell=True)
    cmd = f"docker run --privileged {image} upload -p {port} --fqbn arduino:mbed_nano:nano33ble template"
    subprocess.run([cmd], shell=True)


def upload_rpi():
    "Uploads compiled person detection uf2 file to device. The device must be in the USB Mass Storage Mode and `device_path` should be the absolute path at which the device is mounted at."
    #This can actually get mounted elsewhere, perhaps you could find the path by looking for the files that exist in that directory
    device_path = f"/media/{getpass.getuser()}/RPI-RP2" 
    docker_img = f"{DOCKERHUB_USER}/pico"
    subprocess.run([f"docker pull {docker_img}"], shell=True)
    # this mounts the device_path inside the container and copies the uf2 file from the container to device_path
    cmd = f"docker run --rm -v {device_path}:/opt/mount --entrypoint cp {docker_img} person_detection_screen_int8.uf2 /opt/mount/app.uf2"
    subprocess.run([cmd], shell=True)


def get_device_port(device_name:str):
    return "/dev/ttyACM0"

