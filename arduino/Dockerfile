FROM ubuntu

# tflite-micro
RUN apt update && apt install -y git make unzip curl g++ python3 pip wget netcat
RUN pip3 install Pillow 
RUN git clone https://github.com/tensorflow/tflite-micro.git
WORKDIR tflite-micro
RUN make -j9 -f tensorflow/lite/micro/tools/make/Makefile test_evaluate_cc_test hello_world_bin ADDITIONAL_DEFINES=--coverage

# arduino
WORKDIR ..
RUN curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
RUN arduino-cli core update-index && arduino-cli core install arduino:mbed_nano
RUN arduino-cli lib install Harvard_TinyMLx


COPY template template

# Compile & Upload
ENV DEVICE=/dev/ttyACM0
CMD ["sh", "-c", "arduino-cli compile --fqbn arduino:mbed_nano:nano33ble template && arduino-cli upload -p $DEVICE --fqbn arduino:mbed_nano:nano33ble template"]
