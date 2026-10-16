
from src.my_advanced_lib.core.metaclasses import (
    PluginRegistry,
    GreetingPlugin,
    CalculationPlugin,
    get_plugins,
)


def test_plugins_registered():
    plugins = get_plugins()

    assert "GreetingPlugin" in plugins
    assert "CalculationPlugin" in plugins


def test_plugin_execution():
    assert GreetingPlugin().execute() == "Hello from the plugin!"
    assert CalculationPlugin().execute() == "Calculation plugin executed"


def test_get_plugins_returns_copy():
    plugins = get_plugins()
    plugins.clear()

    assert "GreetingPlugin" in PluginRegistry.plugins


import pytest
from src.my_advanced_lib.core.metaclasses import BasePlugin


def test_base_plugin_execute_raises_error():
    plugin = BasePlugin()

    with pytest.raises(
        NotImplementedError,
        match="Subclasses must implement execute"
    ):
        plugin.execute()

