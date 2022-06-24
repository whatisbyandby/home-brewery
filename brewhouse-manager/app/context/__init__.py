from app.pump.pump import create_pump

def initialize_context(config) -> dict:
    context = {}
    context["pumps"] = {}

    # Initialize pumps
    for pump in config.get("pumps"):
        context["pumps"][pump.get("name")] = (create_pump(pump))

    return context