FROM python:3.9.0-buster

RUN apt update && apt install -y netcat

WORKDIR app
COPY . .
RUN pip3 install -r requirements.txt


CMD ["streamlit", "run", "TinyMLaaS.py"]
#New container for netcat and transfer data to streamlit?
CMD ["nc", "-lp", "8000"


