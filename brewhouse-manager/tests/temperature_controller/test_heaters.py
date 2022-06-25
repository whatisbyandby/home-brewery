from app.temperature_controller.heaters import create_heater, MockHeater, PumpHeater, StandardHeater
from app.pump.pump import MockPump



def test_create_heater():

    heater_config = {"type": "MOCK"}

    mock_heater = create_heater(heater_config=heater_config)
    assert mock_heater is not None
    assert isinstance(mock_heater, MockHeater)

    heater_config = {"type": "STANDARD"}

    standard_heater = create_heater(heater_config=heater_config)
    assert standard_heater is not None
    assert isinstance(standard_heater, StandardHeater)

    pump = MockPump()
    heater_config = {"type": "PUMP_HEATER", "pump": pump}

    pump_heater = create_heater(heater_config=heater_config)
    assert pump_heater is not None
    assert isinstance(pump_heater, PumpHeater)