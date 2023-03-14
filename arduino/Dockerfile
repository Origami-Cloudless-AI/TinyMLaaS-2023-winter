FROM ubuntu

# arduino
RUN apt update && apt install -y curl 
RUN curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
RUN arduino-cli core update-index && arduino-cli core install arduino:mbed_nano
RUN arduino-cli lib install Harvard_TinyMLx


COPY template template

# Compile & Upload
ENV DEVICE=/dev/ttyACM0
CMD ["sh", "-c", "arduino-cli compile --fqbn arduino:mbed_nano:nano33ble template && arduino-cli upload -p $DEVICE --fqbn arduino:mbed_nano:nano33ble template"]
