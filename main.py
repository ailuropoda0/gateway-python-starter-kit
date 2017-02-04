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

import json
import socket
import time
import argparse
import importlib

from cisco_deviot.gateway import Gateway


def class_for_name(mod_name, class_name):
    m = importlib.import_module(mod_name)
    c = getattr(m, class_name)
    return c


def load_configs(filename):
    with open(filename) as json_data:
        return json.load(json_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gateway-python-starter-kit.')
    parser.add_argument('--deviot-server', dest='deviot_server', required=True, type=str,
                        help='url of deviot-server, eg: http://192.168.25.101:9000')
    parser.add_argument('--mqtt-server', dest='mqtt_server', required=True, type=str,
                        help='url of mqtt-server, eg: mqtt://192.168.25.101:1883')
    args = parser.parse_args()

    hostname = socket.gethostname()
    gateway = Gateway(name="ps_" + hostname.lower(),
                      deviot_server=args.deviot_server,
                      connector_server=args.mqtt_server,
                      account="")
    instances = []
    sensors = load_configs('sensors.json')
    for i, sensor in enumerate(sensors):
        name = sensor["name"]
        stype = sensor["type"]
        sid = stype.lower() + "_" + str(i)
        klass = class_for_name("things."+stype, stype.capitalize())
        instance = klass(sid, name)
        if "options" in sensor:
            instance.options = sensor["options"]
        instances.append(instance)
        gateway.register(instance)

    gateway.start()
    while True:
        time.sleep(1)
        data = {}
        for instance in instances:
            if getattr(instance, 'update_state', None):
                instance.update_state()
            instanceData = {}
            for prop in instance.properties:
                instanceData[prop.name] = getattr(instance, prop.name)
            if len(instanceData) != 0:
                data[instance.id] = instanceData
        if len(data) != 0:
            gateway.send_data(data)
