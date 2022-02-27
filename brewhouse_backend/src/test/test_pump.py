from brewhouse_controller import Pump


def test_pump():
    test_pump = Pump()

    test_pump.pump_on()

    assert test_pump.get_pump_status() is True

    test_pump.pump_off()

    assert test_pump.get_pump_status() is False
