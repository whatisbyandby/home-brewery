from hashlib import new
from fastapi import APIRouter, Request, status, Response, Path
from app.pump.pump import Pump, PumpStateRequest

pump_router = APIRouter()


@pump_router.get("/brewhouse/pumps")
async def get_pumps(request: Request):
    return request.app.brewery_controller.components.get("pumps")


@pump_router.get("/brewhouse/pumps/{pump_id}")
async def get_pumps(request: Request, pump_id: str = Path(title="The id of the pump to update")):
    return request.app.brewery_controller.components.get("pumps").get(pump_id)


@pump_router.put("/brewhouse/pumps/{pump_id}")
async def get_pumps(request: Request, update_request: PumpStateRequest, pump_id: str = Path(title="The id of the pump to update")):
    pump: Pump = request.app.brewery_controller.components.get(
        "pumps").get(pump_id)
    new_state = update_request.new_state
    pump.set_pump_state(new_state)
    return pump
