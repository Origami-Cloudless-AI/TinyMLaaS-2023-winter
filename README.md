![GitHub Actions](https://github.com/Origami-TinyML/tflm_hello_world/workflows/workflow/badge.svg)
---
title: "Hello World of TensorFlow Lite for Microcontrollers"
---
Run [Hello World](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world)
example of [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers/get_started_low_level)
in Docker automatically, hooked in CI (Github workflow). You'll implement the following "Test1".

![](tdd.png)

# Slides
- https://github.com/Origami-TinyML/software-engineering-project/blob/artifacts/kickoff.pdf
- https://github.com/Origami-TinyML/software-engineering-project/blob/artifacts/soft_eng_proj_tinyml_lifecycle.md

#  Sprint 1
This time, we'll add training part as WebApp (e.g. [streamlist](https://streamlit.io/)) as Cloud ML.
[This blog](https://blog.devgenius.io/testing-streamlit-a1f1fd48ce8f) helps to implement the following.

1. Train with Jupyter notebook (JN) manucally as explained in TFLm webpage
2. Convert JN to a WebApp with streamlit
3. Observe Hello world output on a WebApp 
4. Add acceptance test & coverage
5. Dockerize the above all, except Jupyter notebook
6. Hook a PR in CI / CD with Github workflow
7. Display the result on Github page
  

# Sprint 0
You can skip training part for now. You need the following steps:

1. git clone <TensorFlow repo>
2. Follow hello world example instruction
3. Run make with appropriate parameter for standalone x86[*](https://www.tensorflow.org/lite/microcontrollers/library#generate_projects_for_other_platforms)
4. Build an executable binary with a model compiled in[*](https://github.com/ehirdoy/tflm)
5. Run an executable binary on x86[*](https://www.tensorflow.org/lite/microcontrollers/library#build_binaries)[*](https://asciinema.org/a/552162)
6. Put the above all in a container, reproducible with Docker file, inc all needed packages with "apt install" & "git clone <TensorFlow repo>" 
7. Add existing unit tests for this hello world[*](https://www.tensorflow.org/lite/microcontrollers/library#run_the_tests)
8. Add test code coverage measurement infrastructure (-gcov in gcc?)
9. Add a new acceptance test, How should we ensure this "Hello world"?
10 Add some dashboard of coverage on github page(?) if no way to present the coverage[*](https://quarto.org/docs/publishing/github-pages.html)
11. Hook a PR in CI / CD (github action / workflow) to run the above all

Please feel free to edit this document to share information with others correctly.

# Sprint 2+
- Convert to a complete TinyML on a VM?  
- Try other ML model?
- Try real HW?
- Try remote CI / CD?
- Try better UI?
