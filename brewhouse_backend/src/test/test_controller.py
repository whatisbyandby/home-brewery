# from datetime import datetime
# from brewhouse_controller import Step
# import pytest


# # def test_compare_temperatures():
# #     controller = BrewhouseController()

# #     # Test Heater Turning On
# #     controller.set_temperature = 10
# #     controller.temp_range = 1
# #     controller.current_temperature = 8.9
# #     controller.mode = TemperatureMode.HEATER
# #     controller.state = ControllerState.IDLE
# #     controller.compare_temperatures()

# #     assert controller.state == ControllerState.HEATING

# #     # Test Heater on the edge of the range
# #     controller.set_temperature = 10
# #     controller.temp_range = 1
# #     controller.current_temperature = 9
# #     controller.mode = TemperatureMode.HEATER
# #     controller.state = ControllerState.IDLE
# #     controller.compare_temperatures()

# #     assert controller.state == ControllerState.IDLE

# #     # Test Heater Turning Off
# #     controller.set_temperature = 10
# #     controller.temp_range = 1
# #     controller.current_temperature = 10
# #     controller.mode = TemperatureMode.HEATER
# #     controller.state = ControllerState.HEATING
# #     controller.compare_temperatures()

# #     assert controller.state == ControllerState.IDLE

# #     # TODO Test the rest of the scanarios

# #     controller.set_temperature = 10
# #     controller.temp_range = 1
# #     controller.current_temperature = 11.1
# #     controller.mode = TemperatureMode.COOLER
# #     controller.compare_temperatures()

# #     assert controller.state == ControllerState.COOLING

# @pytest.mark.asyncio
# async def test_rising_temp():
#     sensor = MockTemperatureSensor([70.1, 70.2, 70.3, 70.4, 70.5])
#     new_step = Step("Mash", 0.15, 'minutes')

#     controller = BrewhouseController(sensors=[sensor], step_list=[new_step])

#     controller.set_temperature = 10
#     start_time = datetime.now()
#     await controller.run()
#     finish_time = datetime.now()

#     assert (finish_time - start_time).total_seconds() > new_step.duration

#     assert (finish_time - start_time).total_seconds() < (new_step.duration * 60) + 1

#     print(controller.current_step.is_completed())
