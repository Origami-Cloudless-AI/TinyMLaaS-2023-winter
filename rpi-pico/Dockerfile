FROM ubuntu as build

#Install Dependencies
RUN apt update && apt install -y python3 pip unzip wget curl git cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential libstdc++-arm-none-eabi-newlib

#Install pico-sdk
RUN git clone -b master https://github.com/raspberrypi/pico-sdk.git
WORKDIR pico-sdk
RUN git submodule update --init
ENV PICO_SDK_PATH=/pico-sdk

#Install latest tflite-micro
RUN git clone https://github.com/tensorflow/tflite-micro
WORKDIR tflite-micro
RUN pip3 install Pillow numpy
RUN python3 tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py src

# Compile person detection
COPY code /code
WORKDIR /code
RUN mkdir build && cd build && cmake ..
WORKDIR build
RUN make -j4

# Replace model and rebuild (most of the build is cached)
COPY model.cc /code/person_detection_screen/person_detect_model_data.cpp 
RUN rm /code/build/person_detection_screen/CMakeFiles/person_detection_screen_int8.dir/person_detect_model_data.cpp.obj
RUN make

# Remove unnecessary files from the docker image
FROM alpine as complete 
COPY --from=build /code/build/person_detection_screen/person_detection_screen_int8.uf2 person_detection_screen_int8.uf2

