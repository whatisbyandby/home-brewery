FROM python:3.9.10

WORKDIR /app

# Install dev dependencies
COPY development.txt development.txt
RUN python -m pip install -r development.txt

# Install dependencies
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

# Copy the Application Code
COPY . .

EXPOSE 5000

CMD [ "python", "./src/main.py" ]