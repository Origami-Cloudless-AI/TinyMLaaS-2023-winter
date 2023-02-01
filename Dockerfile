FROM ubuntu

RUN apt update && apt install -y git make unzip curl g++ python3 pip wget netcat lcov
COPY /build/requirements.txt ./
COPY hello_world.robot ./robot/hello_world.robot

RUN pip3 install -r requirements.txt
RUN git clone https://github.com/tensorflow/tflite-micro.git

CMD ["robot", "./robot/hello_world.robot"]

WORKDIR tflite-micro

RUN make -f tensorflow/lite/micro/tools/make/Makefile test_hello_world_test hello_world_bin ADDITIONAL_DEFINES=--coverage
#RUN gcov -pb -o gen/linux_x86_64_default/obj/core/tensorflow/lite/micro/examples/hello_world tensorflow/lite/micro/examples/hello_world/hello_world_test.cc
#CMD ["mkdir gcovr-report"]
#RUN gcovr --root . --html --html-details --output gcovr-report/coverage.html

#CMD ["./gen/linux_x86_64_default/bin/hello_world_test"]
CMD ./gen/linux_x86_64_default/bin/hello_world 2>&1 | nc -v frontend 50007
