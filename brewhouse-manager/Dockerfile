#############################################
# Base container with all necessary deps
FROM python:3.10 AS base

RUN pip install --upgrade pip

ENV HOME=/code 
WORKDIR ${HOME}
RUN pip install uvicorn[standard]
COPY ./requirements/requirements.txt ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt



#############################################
# Test container from a common base
FROM base AS test
# Same as in the base image but this time we also install the --dev packages
COPY ./requirements/test.txt ./requirements/test.txt
RUN pip install -r ./requirements/test.txt

RUN mkdir ./log
COPY ./config ./config
COPY ./app ./app
COPY ./tests ./tests
COPY ./public ./public

#############################################
# Development container from a common base
FROM base AS development

COPY ./requirements/test.txt ./requirements/test.txt
RUN pip install -r ./requirements/test.txt
COPY ./requirements/plugins.txt ./requirements/plugins.txt
RUN pip install -r ./requirements/plugins.txt

RUN mkdir ./log
COPY ./app ./app
COPY ./config ./config
COPY ./plugins ./plugins
COPY ./public ./public

ENTRYPOINT [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]


#############################################
# Container to Test Plugins container from a common base
FROM test as test_plugins
COPY ./plugins ./plugins
COPY ./requirements/plugins.txt ./requirements/plugins.txt
RUN pip install -r ./requirements/plugins.txt


#############################################
# Final container with the app
FROM base AS production
# Only copy the ready app dir from the live step
COPY  ./requirements/plugins.txt ./requirements/plugins.txt
RUN pip install -r ./requirements/plugins.txt