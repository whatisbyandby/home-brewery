from app.kettle import create_kettle, Kettle
from app.temperature_controller.temperature_controller import TemperatureController, ControllerMode
from app.temperature_controller.heaters import MockHeater
from app.temperature_controller.temperature_sensor import MockSensor
from app.pump.pump import MockPump


def test_create_kettle(config, context):

    kettle_config = config['kettles']['hlt']

    kettle = create_kettle(kettle_config, context=context)
    assert kettle is not None


def test_kettle_init():

    sensors = [MockSensor()]
    mode = ControllerMode.HEATER
    temp_range = 1
    heater = MockHeater()

    temp_controller = TemperatureController(
        sensors=sensors,
        mode=mode,
        temp_range=temp_range,
        heater=heater
    )

    kettle = Kettle(name="Test", temp_controller=temp_controller)


def test_get_current_temp(kettle: Kettle):
    cur_temp = kettle.get_current_temp()
    assert cur_temp is not None
