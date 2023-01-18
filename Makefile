IMAGENAME = hello_world

.PHONY: docker

docker:
	docker build -f Dockerfile.x86 -t ${IMAGENAME} .
