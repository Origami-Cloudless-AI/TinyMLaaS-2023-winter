# Project ideas

Here are some ideas of this project.


## Isolation of Frontend (Streamlit) from Backend REST (Fast API) server

Currently [Streamlit](https://streamlit.io/) includes frontend and backend at once in our implementation.
This architecture should be improved so that Streamlit would include only UI part and
its backend part would include only logic as a rest api server.
Eventually this new architecture would have another UI (e.g. CLI) additionally to control TinyMLaaS as much as the current GUI does.

- https://docs.edgeimpulse.com/reference/edge-impulse-api/edge-impulse-api


## UI polishment

The current Streamlit UI doesn't use a full feature of streamlit capability.
With introducting other Streamlit features, the UI would be improved.
For example, introducing some layout containers would provide consistent impression.
This is a lightweight task.

- https://docs.streamlit.io/library/api-reference/layout
- https://github.com/ddobrinskiy/streamlit-jupyter
- https://discuss.streamlit.io/t/streamlit-in-pyscript/24922



## Add BLE FOTA support

The current Firmware Over The Air update (FOTA) is done via USB.
This could be done via BLE too.

- https://forum.arduino.cc/t/arduino-ble-sense-33-ota-update/983160


## Apply real world use cases

We need some real world use cases to try TinyMLaaS. For example,

- Parking occupancy, https://www.edgeimpulse.com/blog/car-parking-occupancy-detection-using-edge-impulse-fomo
- People counting, https://www.mouser.com/blog/solving-extinction-crisis-edge-ai


## Add new device support

Currently we support only 2 devices, Arduino 33 BLE and Raspberry PI nano. We could add the following device support too.

- Smartphone APP as a pseudo device since Smartphone has many sensors. (HTML5 or JS)
- NordicSemi's Thingy:91, https://www.nordicsemi.com/Products/Development-hardware/Nordic-Thingy-91
- Jetson Nano, https://developer.nvidia.com/embedded/jetson-nano-developer-kit
- RPI, https://www.raspberrypi.com/products/raspberry-pi-4-model-b/


## Arduino Cloud integration

Use "Arduino Cloud" as IoT platform and we would put TinyMLaaS on the top of Arduino Cloud. We need some feasibility study at first.

https://cloud.arduino.cc/
