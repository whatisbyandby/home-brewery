from fastapi import APIRouter, Request, Response, Path
from app.brewery_controller.brewery_controller import KettleUpdate


brewhouse_router = APIRouter()


@brewhouse_router.get("/brewhouse/state")
async def get_brewery_config(request: Request):
    return request.app.brewery_controller


@brewhouse_router.get("/brewhouse/kettles")
async def get_brewehouse_kettles(request: Request):
    kettles = []
    kettle_dict = request.app.brewery_controller.components.get("kettles")
    for key, value in kettle_dict.items():
        kettles.append(value)
    return kettles


@brewhouse_router.get("/brewhouse/kettles/{kettle_id}")
async def get_brewehouse_kettles(request: Request, kettle_id: str = Path(title="The id of the kettle to update")):
    kettles = request.app.brewery_controller.components.get("kettles")
    kettle = kettles.get(kettle_id)
    if kettle is None:
        return Response(status_code=404)
    return kettle


@brewhouse_router.put("/brewhouse/kettles/{kettle_id}")
async def get_brewehouse_kettles(request: Request, kettle_update: KettleUpdate, kettle_id: str = Path(title="The id of the kettle to update")):
    return request.app.brewery_controller.update_kettle(kettle_id, kettle_update)
