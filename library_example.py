
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from src.my_advanced_lib.core.metaclasses import get_plugins

plugins = get_plugins()

print("Registered plugins:")

for name, plugin_class in plugins.items():
    plugin = plugin_class()
    print(name, "->", plugin.execute())
