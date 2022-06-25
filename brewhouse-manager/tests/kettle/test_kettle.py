from app.kettle import create_kettle, Kettle, KettleConfig
from app.temperature_controller.temperature_controller import TemperatureController, ControllerMode
from app.temperature_controller.heaters import MockHeater
from app.temperature_controller.temperature_sensor import MockSensor

def test_create_kettle():
    kettle_config = KettleConfig(name="Test", sensor_config={"type": "MOCK"}, heater_config={"type": "MOCK"})
    kettle = create_kettle(kettle_config=kettle_config)
    assert kettle is not None

def test_kettle_init():

    sensor = MockSensor()
    mode = ControllerMode.HEATER
    temp_range = 1
    heater = MockHeater()

    temp_controller = TemperatureController(
        sensor=sensor, 
        mode=mode,
        temp_range=temp_range,
        heater=heater
        )

    kettle = Kettle(name="Test", temp_controller=temp_controller)