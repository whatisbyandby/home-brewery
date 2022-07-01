# 
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements/requirements.txt /code/requirements.txt
COPY ./requirements/test.txt /code/test.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install -r /code/test.txt

# 
COPY ./app /code/app
COPY ./tests /code/tests



# 
CMD ["pytest", "--cov=app", "--cov-report=html:cover/cov_html", "--ignore=./tests/on_device"]


