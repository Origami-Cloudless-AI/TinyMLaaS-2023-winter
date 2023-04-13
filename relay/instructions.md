# Instructions for using relay/bridging server

## Expose the port with ngrok.
- Run ngrok http {port num} to expose a port for outside traffic

## Server
- Run the main.py to start up the webhook server.

## Initiate the upload process.
- curl -H "Content-Type: application/json" -X POST -d '{"data": "This is some test data"}' {ngrok forwarding ip}/install to make a POST request to the webhook server that triggers uploading.
- Replace the ngrok.io ip address with the one shown in ngrok's forwarding section.
- If 'sudo' is required for docker, you must provide a password in the webhook server side before command runs.

## Misc.
- Arduino dockerfile must be built before hand on the bridging device for now.

## TODO 

- All the docker images must be built and uploaded to some registry in the streamlit app,  e.g., Dockerhub(?)

