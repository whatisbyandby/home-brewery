from fastapi import FastAPI, WebSocket, Response, status, Request
from typing import List
import logging

from app.pump.pump import Pump
from app.temperature_controller.heater import Heater
from app.step_controller.step_controller import StepController
from app.routes.steps import router

app = FastAPI()

logging.basicConfig(filename='./log/app.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s [%(levelname)s-%(name)s] %(message)s')


def initialize_context():
    logging.info("Initializing Brewery Context")
    return {
        "pump_one": Pump("pump_one"),
        "pump_two": Pump("pump_two"),
        "mash_heater": Heater(),
        "hlt_heater": Heater(),
        "boil_heater": Heater(),
        "step_controller": StepController()
    }


app.context = initialize_context()

app.include_router(router)


@app.get("/")
async def home(request: Request):
    logging.info(request.app)
    logging.info("Home page")
    return {"Hello": "World"}
