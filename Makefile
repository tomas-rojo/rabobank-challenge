help:
	@echo ""
	@echo "Options:"
	@echo ""
	@echo "- make install				Install development dependencies"
	@echo "- make help				Show this help"
	@echo "- make test				Run full test suite (flake8 and unit tests)"
	@echo "- make run				Run the application"
	@echo ""
	@echo " DOCKER "
	@echo ""
	@echo "- make build				Build the Docker image"
	@echo "- make test_in_docker			Run the unit tests inside the container"
	@echo "- make start    			Start the application inside the container"
	@echo ""

DOCKER_IMAGE_NAME = rabobank-challenge

install:
	@bin/install_dependencies

test:
	@bin/run_test_suite

run:
	@python3 src/word_frequency_analyzer.py

build:
	@docker buildx build --load -t $(DOCKER_IMAGE_NAME) .

test_in_docker:
	@docker run --rm --volume .:/code $(DOCKER_IMAGE_NAME) tox --colored yes

start:
	@docker run --rm --volume .:/code $(DOCKER_IMAGE_NAME) make run
