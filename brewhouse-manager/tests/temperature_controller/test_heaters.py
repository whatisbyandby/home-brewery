from app.temperature_controller.heaters import create_heater, MockHeater, PumpHeater, StandardHeater
from app.pump.pump import MockPump



def test_create_heater():

    context = {"pumps": {"text_pump": MockPump()}}

    heater_config = {"type": "MOCK"}

    mock_heater = create_heater(heater_config=heater_config, context=context)
    assert mock_heater is not None
    assert isinstance(mock_heater, MockHeater)

    heater_config = {"type": "STANDARD"}

    standard_heater = create_heater(heater_config=heater_config, context=context)
    assert standard_heater is not None
    assert isinstance(standard_heater, StandardHeater)

    
    heater_config = {"type": "PUMP_HEATER", "pump": "text_pump"}

    pump_heater = create_heater(heater_config=heater_config, context=context)
    assert pump_heater is not None
    assert isinstance(pump_heater, PumpHeater)