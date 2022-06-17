# from .mash_controller import MashController, MashStep
# from .pump import MockPump
# from .temperature_controller import MockSensor, MockHeater, TemperatureController, ControllerMode, Timer
# import time

# def test_mash_controller():

#     sensor = MockSensor([60.0, 60.0, 60.0])
#     mock_heater = MockHeater()

#     mock_pump = MockPump()
#     mock_pump_2 = MockPump()

#     temp_controller = TemperatureController(sensor, set_temperature=60.0, mode=ControllerMode.HEATER, heater=mock_heater)

#     saccrification = MashStep("Saccharification", 60.0, 0.25)

#     profile = [saccrification]

#     mash_controller = MashController(
#         profile=profile, 
#         temp_controller=temp_controller, 
#         circulation_pump=mock_pump, 
#         transfer_pump=mock_pump_2)

#     mash_controller.start_mash()
#     time.sleep(30)
