IMAGENAME = hello_world

.PHONY: docker app

docker:
	docker build -f Dockerfile -t ${IMAGENAME} .

app:
	docker-compose up
