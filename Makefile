IMAGENAME = hello_world

.PHONY: docker app

docker:
	docker build -f Dockerfile -t ${IMAGENAME} .

app:
	nbdev_prepare
	docker-compose up --build
