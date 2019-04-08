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


import time
import random
from cisco_deviot.thing import Action, Thing, Property, PropertyType
from cisco_deviot import logger


class Mock_beeper(Thing):
    def __init__(self, tid, name):
        Thing.__init__(self, tid, name, "mock")
        self.add_action(Action("beep").
                        add_parameter(Property(name="duration", type=PropertyType.INT, value=10, range=[10, 100])).
                        add_parameter(Property(name="interval", type=PropertyType.INT, value=1, range=[1, 10])))
        self.options = {}

    def beep(self, duration, interval):
        if not isinstance(duration, int):
            duration = int(duration)
        if not isinstance(interval, int):
            interval = int(interval)
        elapsed_time = 0
        while elapsed_time < duration:
            logger.info("[BEEP]")
            time.sleep(interval)
            elapsed_time += interval
