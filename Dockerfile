FROM ubuntu

RUN apt update && apt install -y git make unzip curl g++ python3 pip wget
RUN pip3 install Pillow Wave
RUN git clone https://github.com/tensorflow/tflite-micro.git

WORKDIR tflite-micro
RUN make -f tensorflow/lite/micro/tools/make/Makefile test_hello_world_test

CMD ["./gen/linux_x86_64_default/bin/hello_world_test"]
