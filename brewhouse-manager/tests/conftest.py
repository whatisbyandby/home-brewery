import pytest
from app.temperature_controller.temperature_controller import TemperatureController, ControllerMode
from app.kettle import Kettle
from app.temperature_controller.temperature_sensor import MockSensor
from app.temperature_controller.heaters import MockHeater


@pytest.fixture
def context():
    return {
        "plugins": [],
        "pumps": {
            "water_pump": {
                "name": "water",
                "pump_type": "STANDARD",
                "pin": {
                    "pin_num": 18,
                    "pin_type": "MOCK"
                }
            },
            "wort_pump": {
                "name": "wort",
                "pump_type": "STANDARD",
                "pin": {
                    "pin_num": 19,
                    "pin_type": "MOCK"
                }
            }
        },
        "temp_sensors": {
            "hlt_temp": {
                "id": "hlt_temp",
                "type": "MOCK",
                "pin_number": 3
            },
            "mash_temp": {
                "id": "mash_temp",
                "type": "MOCK",
                "pin_number": 4
            },
            "rims_temp": {
                "id": "rims_temp",
                "type": "MOCK",
                "pin_number": 5
            },
            "boil_temp": {
                "id": "boil_temp",
                "type": "MOCK",
                "pin_number": 6
            }
        },
        "heaters": {
            "hlt_heater": {
                "id": "htl_heater",
                "type": "STANDARD",
                "pin": {
                    "pin_num": 24,
                    "pin_type": "MOCK"
                }
            },
            "rims_heater": {
                "id": "htl_heater",
                "type": "PUMP_HEATER",
                "pin": {
                    "pin_num": 25,
                    "pin_type": "MOCK"
                },
                "pump": "wort_pump"
            },
            "boil_heater": {
                "id": "boil_heater",
                "type": "STANDARD",
                "pin": {
                    "pin_num": 26,
                    "pin_type": "MOCK"
                }
            }
        },
        "kettles": {
            "hlt": {
                "id": "hlt",
                "name": "Hot Liquor Tank",
                "temperature_controller": {
                    "sensors": [
                        "hlt_temp"
                    ],
                    "heater": "hlt_heater"
                }
            },
            "mash_tun": {
                "id": "mash_tun",
                "name": "Mash Tun",
                "temperature_controller": {
                    "sensors": [
                        "mash_temp",
                        "rims_temp"
                    ],
                    "heater": "rims_heater"
                }
            },
            "boil": {
                "id": "boil",
                "name": "Boil Kettle",
                "temperature_controller": {
                    "sensors": [
                        "boil_temp"
                    ],
                    "heater": "boil_heater"
                }
            }
        }
    }


@pytest.fixture
def config():
    return {
        "plugins": [],
        "pins": {
            "water_pump_pin": {
                "pin_num": 18,
                "pin_type": "MOCK"
            },
            "water_pump_pin": {
                "pin_num": 18,
                "pin_type": "MOCK"
            }
        },
        "pumps": {
            "water_pump": {
                "name": "water",
                "pump_type": "STANDARD",
                "pin": "water_pump_pin"
            },
            "wort_pump": {
                "name": "wort",
                "pump_type": "STANDARD",
                "pin": "water_pump_pin"
            }
        },
        "temp_sensors": {
            "hlt_temp": {
                "sensor_type": "MOCK",
                "pin_number": 3
            },
            "mash_temp": {
                "sensor_type": "MOCK",
                "pin_number": 4
            },
            "rims_temp": {
                "sensor_type": "MOCK",
                "pin_number": 5
            },
            "boil_temp": {
                "sensor_type": "MOCK",
                "pin_number": 6
            }
        },
        "heaters": {
            "hlt_heater": {
                "id": "htl_heater",
                "type": "STANDARD",
                "pin": {
                    "pin_num": 24,
                    "pin_type": "MOCK"
                }
            },
            "rims_heater": {
                "id": "htl_heater",
                "type": "PUMP_HEATER",
                "pin": {
                    "pin_num": 25,
                    "pin_type": "MOCK"
                },
                "pump": "wort_pump"
            },
            "boil_heater": {
                "id": "boil_heater",
                "type": "STANDARD",
                "pin": {
                    "pin_num": 26,
                    "pin_type": "MOCK"
                }
            }
        },
        "kettles": {
            "hlt": {
                "id": "hlt",
                "name": "Hot Liquor Tank",
                "temperature_controller": {
                    "sensors": [
                        "hlt_temp"
                    ],
                    "heater": "hlt_heater"
                }
            },
            "mash_tun": {
                "id": "mash_tun",
                "name": "Mash Tun",
                "temperature_controller": {
                    "sensors": [
                        "mash_temp",
                        "rims_temp"
                    ],
                    "heater": "rims_heater"
                }
            },
            "boil": {
                "id": "boil",
                "name": "Boil Kettle",
                "temperature_controller": {
                    "sensors": [
                        "boil_temp"
                    ],
                    "heater": "boil_heater"
                }
            }
        }
    }


@pytest.fixture
def kettle():
    sensors = [MockSensor()]
    mode = ControllerMode.HEATER
    temp_range = 1
    heater = MockHeater()

    temp_controller = TemperatureController(
        sensors=sensors,
        mode=mode,
        temp_range=temp_range,
        heater=heater
    )

    return Kettle(name="Test", temp_controller=temp_controller)
