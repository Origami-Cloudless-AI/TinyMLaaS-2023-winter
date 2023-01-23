FROM python:3.9.0-buster

WORKDIR app
COPY . .
RUN pip3 install -r requirements.txt

CMD ["streamlit", "run", "TinyMLaaS.py"]
