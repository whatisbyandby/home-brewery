from fastapi import APIRouter, Request, status, Response
from json.decoder import JSONDecodeError
from typing import List
from app.step_controller.step_controller import Step

router = APIRouter()


@router.get("/steps", status_code=200)
async def get_steps(request: Request):
    return request.app.context.get("step_controller").get_steps()


@router.post("/steps", status_code=200)
async def post_steps(request: Request, response: Response, steps: List[Step]):
    try:
        return request.app.context.get("step_controller").set_steps(steps)
    except JSONDecodeError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Invalid JSON"}


@router.get("/steps/current", status_code=200)
async def get_current_step(request: Request):
    return request.app.context.get("step_controller").get_current_step()
