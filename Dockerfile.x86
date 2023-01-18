FROM python:3.9.0-buster

RUN apt-get update

RUN pip3 install Pillow
RUN git clone https://github.com/tensorflow/tflite-micro.git

WORKDIR tflite-micro
RUN make -f tensorflow/lite/micro/tools/make/Makefile hello_world_bin

CMD ["./gen/linux_x86_64_default/bin/hello_world"]

