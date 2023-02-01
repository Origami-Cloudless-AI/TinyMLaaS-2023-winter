FROM ubuntu

RUN apt update && apt install -y git make unzip curl g++ python3 pip wget
COPY /build/requirements.txt ./
COPY hello_world.robot ./robot/hello_world.robot
COPY hello_world_test.py ./test/hello_world_test.py

RUN pip3 install -r requirements.txt
RUN git clone https://github.com/tensorflow/tflite-micro.git

WORKDIR tflite-micro

RUN make -f tensorflow/lite/micro/tools/make/Makefile test_hello_world_test hello_world_bin ADDITIONAL_DEFINES=--coverage
RUN gcov -pb -o gen/linux_x86_64_default/obj/core/tensorflow/lite/micro/examples/hello_world tensorflow/lite/micro/examples/hello_world/hello_world_test.cc

#RUN pip3 install codecov
#RUN codecov

#CMD ["./gen/linux_x86_64_default/bin/hello_world"]
CMD ["./gen/linux_x86_64_default/bin/hello_world_test"]

WORKDIR /

CMD ["robot", "./robot/hello_world.robot"]
RUN pytest test
