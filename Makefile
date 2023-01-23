IMAGENAME = hello_world

.PHONY: docker

docker:
	docker build -f Dockerfile -t ${IMAGENAME} .

app:
	streamlit run TinyMLaaS.py
