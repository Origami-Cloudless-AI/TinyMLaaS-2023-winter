IMAGENAME = hello_world

.PHONY: docker app backend

docker:
	docker build -f Dockerfile -t ${IMAGENAME} .

app:
	nbdev_prepare
	docker-compose up --build

backend:
	docker build -t backend backend
	docker run -p 8080:8080 backend
