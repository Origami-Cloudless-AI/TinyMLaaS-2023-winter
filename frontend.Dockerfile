FROM python:3.9.0-buster


WORKDIR app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .


CMD ["streamlit", "run", "TinyMLaaS.py"]


