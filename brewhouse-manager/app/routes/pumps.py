from fastapi import APIRouter, Request, status, Response, Path
from app.pump.pump import Pump, PumpStateRequest

pump_router = APIRouter()


@pump_router.get("/brewhouse/pumps")
async def get_pumps(request: Request):
    pumps = []
    retrieved_pumps = request.app.brewery_controller.components.get("pumps")
    for pump in retrieved_pumps.values():
        cur_pump = {
            "name": pump.name,
            "state": pump.get_state()
        }
        pumps.append(cur_pump)
    return pumps


@pump_router.get("/brewhouse/pumps/{pump_id}")
async def get_pump(request: Request, pump_id: str = Path(title="The id of the pump to update")):
    return request.app.brewery_controller.components.get("pumps").get(pump_id)


@pump_router.put("/brewhouse/pumps/{pump_id}")
async def update_pump(request: Request, update_request: PumpStateRequest, pump_id: str = Path(title="The id of the pump to update")):
    pump: Pump = request.app.brewery_controller.components.get(
        "pumps").get(pump_id)
    new_state = update_request.new_state
    pump.set_pump_state(new_state)
    return pump
