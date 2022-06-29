import logging
import json
import os
from dotenv import load_dotenv

from app.context import initialize_context
from app.pins.pin import create, start_pins
from .app import create_server

load_dotenv()


logging.basicConfig(filename='./log/app.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s [%(levelname)s-%(name)s] %(message)s')


def get_config(path: str):
    with open(path, "r") as config_file:
        return json.load(config_file)


config_file = os.getenv("CONFIG_FILE")
config = get_config(config_file)
start_pins()
context = initialize_context(config=config)

app = create_server(context=context)
