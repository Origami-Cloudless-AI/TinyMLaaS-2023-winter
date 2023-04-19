# Instructions for using relay/bridging server

## Expose the port with ngrok.
- Run ngrok http {port num} to expose a port for outside traffic
- Pass the ngrok forwarding ip to streamlit in the device page.

## Server
- Run the main.py to start up the webhook server.

## Misc.
- Arduino dockerfile must be built before hand on the bridging device for now.
- Streamlit app must be logged in to docker in order to push images to hub.
- Pushing images is disabled for now and uploading uses the existing image in the dockerhub.
- Code exists for tagging and uploading the images to dockerhub.

## TODO
- Implement rest of the necessary routes for the webhook.
 
