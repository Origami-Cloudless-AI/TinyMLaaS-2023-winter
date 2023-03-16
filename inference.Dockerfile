FROM python:3.9.0-slim-buster

ARG model_path_arg defalt_model_value
ARG image_path_arg default_image_value

RUN apt update && apt install -y git make g++ python3 libgl1 libglib2.0-0

COPY $model_path $model_path
COPY $image_path $image_path


RUN pip3 install --upgrade pip
COPY x86_simulation/requirements-app.txt .
RUN pip3 install -r requirements-app.txt
COPY x86_simulation/inference.py .
CMD ["python3", "inference.py"]

#Docker build -t inference --build-arg model_path=models/model_no_quant.tflite --build-arg=image_path=data/1/24.png -f inference.Dockerfile .
#Docker run -e model_path="path to the model.tflite in this container i.e. the same as in the host" -e image_path="path to the image for inference" inference
