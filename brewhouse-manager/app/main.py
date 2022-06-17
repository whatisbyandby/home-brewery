from fastapi import FastAPI, WebSocket, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dataclasses import dataclass
import json
from typing import List
import os

app = FastAPI()

class MashStep(BaseModel):
    temp: float
    duration: int

class MashProfile(BaseModel):
    name: str
    description: str
    steps: List[MashStep]

class Recipe(BaseModel):
    name: str
    description: str
    mash_profile: MashProfile

@app.on_event("startup")
async def startup_event():
    engine = db.create_engine('sqlite:///data/brewhouse.db')
    engine.connect()
    
    
@app.get("/")
async def home():
    return {"Hello": "World"}

@app.get("/recipe")
async def get_recipe(recipe: Recipe, response: Response):
    try:
        with open("./data/recipe.json", "r") as existing_file:
            existing_recipe = json.load(existing_file)
            return existing_recipe
    except FileNotFoundError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "No Current Recipe Set"}


@app.post("/recipe")
async def post_recipe(recipe: Recipe, response: Response):
    cursor = connection.cursor()
    print(connection.total_changes)
    return "Hello World"
    

@app.delete("/recipe")
async def delete_recipe(response: Response):
    try:
        os.remove("./data/recipe.json")
        return {"message": "Recipe removed"}
    except FileNotFoundError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "No recipe is set"}



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
