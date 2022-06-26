from app.brewery_controller.brewery_controller import BreweryController


def test_initalizer():
    components = {}
    brewery_controller = BreweryController(components=components)

    assert brewery_controller is not None
