import pytest
from app.pump.pump import CreatePumpError, create_pump, MockPump, StandardPump
from app.pins.pin import MockPin


def test_create_pump():

    pump_config = {
        "name": "water",
        "pump_type": "MOCK",
        "pin": {
            "pin_num": 18,
            "pin_type": "MOCK"
        }
    }

    mock_pump = create_pump(pump_config=pump_config)
    assert mock_pump is not None
    assert isinstance(mock_pump, MockPump)

    pump_config = {
        "name": "water",
        "pump_type": "NOT_REAL",
        "pin": {
            "pin_num": 18,
            "pin_type": "MOCK"
        }
    }

    with pytest.raises(CreatePumpError):
        mock_pump = create_pump(pump_config=pump_config)


def test_standard_pump():
    mock_pin = MockPin(pin_num=18)

    standard_pump = StandardPump(name="Test Standard", pin=mock_pin)

    assert standard_pump is not None

    standard_pump.pump_on()
    assert mock_pin.get_state() is True

    standard_pump.pump_off()
    assert mock_pin.get_state() is False

    assert standard_pump.get_state() is False
