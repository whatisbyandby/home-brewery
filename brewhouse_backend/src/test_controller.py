from controller import BrewhouseController, TemperatureMode, ControllerState


def test_compare_temperatures():
    controller = BrewhouseController()

    # Test Heater Turning On
    controller.set_temperature = 10
    controller.temp_range = 1
    controller.current_temperature = 8.9
    controller.mode = TemperatureMode.HEATER
    controller.state = ControllerState.IDLE
    controller.compare_temperatures()

    assert controller.state == ControllerState.HEATING

    # Test Heater on the edge of the range
    controller.set_temperature = 10
    controller.temp_range = 1
    controller.current_temperature = 9
    controller.mode = TemperatureMode.HEATER
    controller.state = ControllerState.IDLE
    controller.compare_temperatures()

    assert controller.state == ControllerState.IDLE

    # Test Heater Turning Off
    controller.set_temperature = 10
    controller.temp_range = 1
    controller.current_temperature = 10
    controller.mode = TemperatureMode.HEATER
    controller.state = ControllerState.HEATING
    controller.compare_temperatures()

    assert controller.state == ControllerState.IDLE

    # TODO Test the rest of the scanarios

    controller.set_temperature = 10
    controller.temp_range = 1
    controller.current_temperature = 11.1
    controller.mode = TemperatureMode.COOLER
    controller.compare_temperatures()

    assert controller.state == ControllerState.COOLING
