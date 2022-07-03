from app.context import initialize_context

# Some Comments to make sure the tests run


def test_initialize_context(config):

    context = initialize_context(config)

    # Assert the pumps were initialized
    pins = context.get("pins")
    assert pins is not None

    pumps = context.get("pumps")
    assert pumps is not None

    temp_sensors = context.get("temp_sensors")
    assert temp_sensors is not None

    heaters = context.get("heaters")
    assert heaters is not None

    kettles = context.get("kettles")
    assert kettles is not None
