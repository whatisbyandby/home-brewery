from fastapi import FastAPI, WebSocket, Response, status, Request, Path
import logging

from app.routes.steps import step_router
from app.routes.brewhouse import brewhouse_router
from app.context import initialize_context
from app.brewery_controller.brewery_controller import BreweryController
from app.pins.pin import initalize_pins
import json

app = FastAPI()

logging.basicConfig(filename='./log/app.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s [%(levelname)s-%(name)s] %(message)s')


def get_config(path: str):
    with open(path, "r") as config_file:
        return json.load(config_file)


config = get_config("./app/config/config.json")
context = initialize_context(config=config)
initalize_pins()

app.brewery_controller = BreweryController(components=context)

app.include_router(step_router)
app.include_router(brewhouse_router)


@app.get("/")
async def home(request: Request):
    logging.info(request.app)
    logging.info("Home page")
    return {"Hello": "World"}
