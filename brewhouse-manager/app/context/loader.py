"""The plugin loader for the brewery controller"""

import importlib


class PluginInterface:

    @staticmethod
    def initalize() -> None:
        """Initalize the plugin"""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)


def load_plugins(plugins: list[str]) -> None:
    """Load the plugins from the plugin list"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initalize()
