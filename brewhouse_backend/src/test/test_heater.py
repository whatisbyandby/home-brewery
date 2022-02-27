from brewhouse_controller import Heater


def test_heater():
    heater = Heater(1)
    heater.heater_on()
    assert heater.get_heater_status() is True
    heater.heater_off()
    assert heater.get_heater_status() is False
