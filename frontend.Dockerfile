FROM python:3.9.0-slim-buster

RUN apt-get update && apt-get install curl libportaudio2 libusb-1.0 graphviz python3-opencv xxd -y
WORKDIR app
ADD data /data/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN curl -fsSL https://get.docker.com | sh

COPY . .

CMD ["python3", "-m", "coverage", "run", "--source=pages,tflm_hello_world" , "-m", "streamlit", "run", "TinyMLaaS.py", "--server.headless", "true"]
