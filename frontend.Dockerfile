FROM python:3.9.0-slim-buster

RUN apt-get update && apt-get install libportaudio2 libusb-1.0 python3-opencv -y
WORKDIR app
ADD data /data/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .


CMD ["streamlit", "run", "TinyMLaaS.py"]
