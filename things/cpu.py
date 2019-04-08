import time
import os

from cisco_deviot.thing import Action, Thing, Property, PropertyType
from cisco_deviot import logger

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    import psutil
except ImportError as e:
    install('psutil')

class Cpu(Thing):
    def __init__(self, tid, name):
        Thing.__init__(self, tid, name, "cpu")
        self.add_property(Property(name="CPU_usage", unit="%"))
        self.add_property(Property(name="memory_usage", unit="%"))

    def update_state(self):
        self.update_property(CPU_usage=psutil.cpu_percent(), memory_usage=psutil.virtual_memory().percent)
