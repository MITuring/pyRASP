import importlib
import sys


# reload modules
loaded_modules = []
for module in sys.modules:
    loaded_modules.append(module)

for module in loaded_modules:
    importlib.reload(sys.modules[module])

