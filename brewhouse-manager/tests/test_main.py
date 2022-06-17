# from fastapi.testclient import TestClient
# from .main import app
# import os

# client = TestClient(app)

# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"Hello": "World"}

# def test_post_recipe():
#     os.remove("./data/recipe.json")
#     response = client.post("/recipe", json={
#     "name": "Recipe Name",
#     "description": "Description",
#     "mash_profile": {
#         "name": "Mash Profile",
#         "description": "Test",
#         "steps": [
#             {
#                 "temp": 150.0,
#                 "duration": 60
#             }
#         ]
#     }
# })
#     assert response.status_code == 201
#     assert response.json() == {"message": "Recipe Stored"}

# def test_get_recipe():
#     response = client.get("/recipe")
#     assert response.status_code == 200
#     assert response.json() == {
#     "name": "Recipe Name",
#     "description": "Description",
#     "mash_profile": {
#         "name": "Mash Profile",
#         "description": "Test",
#         "steps": [
#             {
#                 "temp": 150.0,
#                 "duration": 60
#             }
#         ]
#     }
# }
