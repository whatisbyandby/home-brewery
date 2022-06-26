from app.pump.pump import create_pump
from app.temperature_controller.temperature_sensor import create_sensor
from app.temperature_controller.heaters import create_heater
from app.kettle import create_kettle, KettleConfig


def initialize_context(config) -> dict:
    context = {}
    context["pumps"] = {}
    context["temp_sensors"] = {}
    context["heaters"] = {}
    context["kettles"] = {}

    # Initialize pumps
    for key, value in config.get("pumps").items():
        context["pumps"][key] = create_pump(value)

    # Initalize Sensors
    for key, value in config.get("temp_sensors").items():
        context["temp_sensors"][key] = create_sensor(value)

    # Initalize Sensors
    for key, value in config.get("heaters").items():
        context["heaters"][key] = create_heater(value, context)
    
    # # Initialize kettles
    # for kettle in config.get("kettles"):
    #     temperature_controller = kettle.get('temperature_controller')
    #     sensors = temperature_controller.get("sensors")

    #     sensors = list(sensors)
    #     heater_config = temperature_controller.get("heater")
    #     heater = create_heater(heater_config)

    #     kettle_config = KettleConfig(name=kettle.get("name"), sensor_config=sensors[0], heater_config=heater_config)

    #     new_kettle = create_kettle(kettle_config)

    #     context["kettles"][kettle.get("id")] = new_kettle
        

    return context