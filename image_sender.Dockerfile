# Temporary container to demonstrate sending an image to the backend

FROM ubuntu

RUN apt update && apt install -y git make unzip curl g++ python3 pip wget netcat

COPY tdd.png .

CMD sleep 5 && sha1sum tdd.png > checksum && curl -X POST -F "sha1checksum=@checksum" -F "file_name=@tdd.png" http://backend:8080/upload_image

