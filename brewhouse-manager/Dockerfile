#############################################
# Base container with all necessary deps
FROM python:3.10 AS base

RUN pip install --upgrade pip

ENV HOME=/code 
WORKDIR ${HOME}

COPY ./requirements/requirements.txt ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt
RUN mkdir ./log
COPY ./app ./app
COPY ./config ./config


#############################################
# Test container from a common base
FROM base AS test
# Same as in the base image but this time we also install the --dev packages
COPY ./requirements/test.txt ./requirements/test.txt
RUN pip install -r ./requirements/test.txt
COPY ./tests ./tests

#############################################
# Test container from a common base
FROM test AS development
COPY ./requirements/device.txt ./requirements/device.txt
RUN pip install -r ./requirements/device.txt
COPY ./plugins ./plugins
ENTRYPOINT [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]


#############################################
FROM test as test_plugins
COPY ./plugins /code/plugins
COPY ./requirements/device.txt ./requirements/device.txt
RUN pip install -r ./requirements/device.txt


#############################################
# Final container with the app
FROM base AS production
# Only copy the ready app dir from the live step
COPY  ./requirements/device.txt ./requirements/device.txt
RUN pip install -r ./requirements/device.txt