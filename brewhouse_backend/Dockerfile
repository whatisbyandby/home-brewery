FROM python:3.9.10

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

# Copy the Application Code
COPY . .

EXPOSE 5000

ENTRYPOINT [ "python", "./src/main.py" ]