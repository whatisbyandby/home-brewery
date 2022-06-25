from app.temperature_controller.temperature_sensor import MockSensor
from app.temperature_controller.heaters import MockHeater
from .mock_cooler import MockCooler
from app.temperature_controller.temperature_controller import TemperatureController, ControllerMode, TemperatureState, ControllerState


def test_temperature_controller():

    sensor = MockSensor([60.0, 60.0, 60.0])
    mock_heater = MockHeater()

    temp_controller = TemperatureController(
        sensor, mode=ControllerMode.HEATER, heater=mock_heater)



def test_compare_temperature():
    sensor = MockSensor([50.0, 59.1, 60.1, 61.0])
    mock_heater = MockHeater()

    temp_controller = TemperatureController(
        sensor, mode=ControllerMode.HEATER, heater=mock_heater)

    temp_controller.update_set_temp(60)

    temp_state = temp_controller.compare_temperature()
    assert temp_state == TemperatureState.UNDER_TEMP

    temp_state = temp_controller.compare_temperature()
    assert temp_state == TemperatureState.IN_RANGE_UNDER

    temp_state = temp_controller.compare_temperature()
    assert temp_state == TemperatureState.IN_RANGE_OVER

    temp_state = temp_controller.compare_temperature()
    assert temp_state == TemperatureState.OVER_TEMP


def test_tick():
    heater_sensor = MockSensor([50.0, 59.9, 60.0, 60.1])
    mock_heater = MockHeater()

    heater_temp_controller = TemperatureController(
        heater_sensor, mode=ControllerMode.HEATER, heater=mock_heater)

    heater_temp_controller.update_set_temp(60.0)

    heater_cases = [
        {"current_temperature": 50.0, "mode": ControllerMode.HEATER,
            "set_temperature": 60.0, "state": ControllerState.HEATER_ON},
        {"current_temperature": 59.9, "mode": ControllerMode.HEATER,
            "set_temperature": 60.0, "state": ControllerState.HEATER_ON},
        {"current_temperature": 60.0, "mode": ControllerMode.HEATER,
            "set_temperature": 60.0, "state": ControllerState.ALL_OFF},
        {"current_temperature": 60.1, "mode": ControllerMode.HEATER,
            "set_temperature": 60.0, "state": ControllerState.ALL_OFF}
    ]

    for case in heater_cases:
        current_state = heater_temp_controller.tick()
        assert_cases(case, current_state)

    cooler_sensor = MockSensor([70.0, 60.1, 59.9, 59.0])
    mock_cooler = MockCooler()
    cooler_temp_controller = TemperatureController(
        cooler_sensor, mode=ControllerMode.COOLER, cooler=mock_cooler)

    cooler_temp_controller.update_set_temp(60.0)

    cooler_cases = [
        {"current_temperature": 70.0, "mode": ControllerMode.COOLER,
            "set_temperature": 60.0, "state": ControllerState.COOLER_ON},
        {"current_temperature": 60.1, "mode": ControllerMode.COOLER,
            "set_temperature": 60.0, "state": ControllerState.COOLER_ON},
        {"current_temperature": 59.9, "mode": ControllerMode.COOLER,
            "set_temperature": 60.0, "state": ControllerState.ALL_OFF},
        {"current_temperature": 59.0, "mode": ControllerMode.COOLER,
            "set_temperature": 60.0, "state": ControllerState.ALL_OFF}
    ]

    for case in cooler_cases:
        current_state = cooler_temp_controller.tick()
        assert_cases(case, current_state)


def assert_cases(case, current_state):
    assert current_state is not None
    assert current_state.get("current_temperature") is not None
    assert case.get("current_temperature") == current_state.get(
        "current_temperature")
    assert case.get("mode") == current_state.get("mode")
    assert case.get("set_temperature") == current_state.get("set_temperature")
    assert case.get("state") == current_state.get("state")
