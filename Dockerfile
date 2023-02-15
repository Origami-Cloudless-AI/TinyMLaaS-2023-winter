FROM ubuntu

RUN apt update && apt install -y git make unzip curl g++ python3 pip wget netcat
COPY /build/requirements.txt ./
COPY hello_world.robot ./robot/hello_world.robot
CMD ["robot", "./robot/hello_world.robot"]

RUN pip3 install -r requirements.txt
RUN git clone https://github.com/tensorflow/tflite-micro.git

WORKDIR tflite-micro

RUN make -f tensorflow/lite/micro/tools/make/Makefile test_hello_world_test hello_world_bin ADDITIONAL_DEFINES=--coverage
RUN gcov -pb -o gen/linux_x86_64_default/obj/core/tensorflow/lite/micro/examples/hello_world tensorflow/lite/micro/examples/hello_world/hello_world_test.cc


CMD ["./gen/linux_x86_64_default/bin/hello_world_test"]
CMD sleep 5 && ./gen/linux_x86_64_default/bin/hello_world 2>&1 | nc -v frontend 50007

