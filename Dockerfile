FROM docker.io/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a virtualenv for python packages, without
# triggering the ugly "WARNING: Running pip as the 'root' user can result
# in broken permissions and conflicting behaviour".

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

# Install requirements
RUN apt update && apt install -y \
    make

COPY requirements.txt /tmp
RUN python3 -m pip install -r /tmp/requirements.txt

WORKDIR /code


CMD ["/bin/bash"]
