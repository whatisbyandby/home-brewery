from app.brewery_controller.brewery_controller import BreweryController
from app.pump.pump import MockPump

def test_run_step():
    
    pump_one = MockPump()
    pump_two = MockPump()

    brewery_controller = BreweryController(pump_one=pump_one, pump_two=pump_two)

