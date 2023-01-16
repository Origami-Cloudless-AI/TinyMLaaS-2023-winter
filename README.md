# Hello World of TensorFlow Lite for Microcontrollers

Run [Hello World](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world) example of [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers/get_started_low_level) in Docker automatically. You can skip training part for now.

# TODO
Probably you need the following steps:

1. git clone TensorFlow repo
2. Follow hello world example instruction
3. Run make with appropriate parameter for standalone x86[*](https://www.tensorflow.org/lite/microcontrollers/library#generate_projects_for_other_platforms)
4. Build an executable binary with a model compiled in
5. Run an executable binary on x86[*](https://www.tensorflow.org/lite/microcontrollers/library#build_binaries)
6. Put the above all in a container, reproducible with Docker file
7. Add an unit test for this hello world[*](https://www.tensorflow.org/lite/microcontrollers/library#run_the_tests)
8. Add coverage measurement infrastructure (gcov in C?)
9. Add dashboard of coverage (github page?)
10. Hook PR in CI / CD (github action / workflow)
11. Anything more here?

Please feel free to edit this document to share information with others correctly.
