#############################################
# Base container with all necessary deps
FROM python:3.10 AS base

ENV HOME=/code 
WORKDIR ${HOME}

COPY ./requirements/requirements.txt ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt
RUN mkdir ./log
COPY ./app ./app


#############################################
# Test container from a common base
FROM base AS test
# Same as in the base image but this time we also install the --dev packages
COPY ./requirements/test.txt ./requirements/test.txt
RUN pip install -r ./requirements/test.txt
COPY ./tests ./tests


#############################################
# Final container with the app
FROM base AS production
# Only copy the ready app dir from the live step
COPY  ./requirements/device.txt ./requirements/device.txt
RUN pip install -r ./requirements/device.txt