from app.pump.pump import initalize_pumps
from app.pins.pin import initalize_pins
from .loader import load_plugins
from app.temperature_controller.temperature_sensor import initalize_temp_sensors
from app.temperature_controller.heaters import create_heater
from app.kettle import create_kettle


def initialize_context(config) -> dict:

    load_plugins(config["plugins"])

    context = {}
    context["pins"] = initalize_pins(config)
    context["pumps"] = initalize_pumps(config, context=context)
    context["temp_sensors"] = initalize_temp_sensors(config=config)
    context["heaters"] = {}
    context["kettles"] = {}

    # Initalize Sensors
    for key, value in config.get("temp_sensors").items():
        context["temp_sensors"][key] = create_sensor(value)

    # Initalize Heaters
    for key, value in config.get("heaters").items():
        context["heaters"][key] = create_heater(value, context)

    # Initialize kettles
    for key, value in config.get("kettles").items():
        context["kettles"][key] = create_kettle(value, context)

    return context
