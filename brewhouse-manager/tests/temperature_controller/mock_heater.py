from app.temperature_controller.heater import create_heater


def test_create_heater():

    heater = create_heater(heater_type="MOCK")