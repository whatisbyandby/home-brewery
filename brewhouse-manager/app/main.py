import logging
import json
import os
from dotenv import load_dotenv

from app.context import initialize_context
from .app import create_server

load_dotenv()


logging.basicConfig(filename='./log/app.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s [%(levelname)s-%(name)s] %(message)s')


def get_config():
    with open("./config/config.json", "r") as config_file:
        return json.load(config_file)


config = get_config()
logging.info(config)
context = initialize_context(config=config)

app = create_server(context=context)
