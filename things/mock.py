# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import random
from cisco_deviot.thing import Action, Thing, Property, PropertyTypeInt
from cisco_deviot import logger


class Mock(Thing):
    def __init__(self, tid, name):
        Thing.__init__(self, tid, name, "mock")
        self.add_property(Property("value", PropertyTypeInt))
        self.add_action(Action("beep").
                        add_parameter(Property(name="duration", value=10, range=[10, 100])).
                        add_parameter(Property(name="interval", value=1, range=[1, 10])))
        self.value = 0
        self.options = {}

    def update_state(self):
        vmin = self.options.get("min", 1)
        vmax = self.options.get("max", 100)
        self.value = random.randint(vmin, vmax)

    def beep(self, duration, interval):
        logger.info("[BEEP] {duration} {interval} ".format(duration=duration, interval=interval))
