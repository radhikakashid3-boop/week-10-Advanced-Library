
class PluginRegistry(type):
    """Automatically register plugin classes."""

    plugins = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        if not namespace.get("is_base", False):
            mcs.plugins[name] = cls

        return cls


class BasePlugin(metaclass=PluginRegistry):
    is_base = True

    def execute(self):
        raise NotImplementedError(
            "Subclasses must implement execute()"
        )


class GreetingPlugin(BasePlugin):
    def execute(self):
        return "Hello from the plugin!"


class CalculationPlugin(BasePlugin):
    def execute(self):
        return "Calculation plugin executed"


def get_plugins():
    """Return all registered plugins."""
    return PluginRegistry.plugins.copy()

