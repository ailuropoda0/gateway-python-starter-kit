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
import traceback

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
    parser.add_argument('--deviot-server', dest='deviot_server', type=str,
                        help='url of deviot-server, eg: deviot.cisco.com')
    parser.add_argument('--mqtt-server', dest='mqtt_server', type=str,
                        help='url of mqtt-server, eg: deviot.cisco.com:18883')
    parser.add_argument('--account', dest="account", required=True, type=str, help='your account on DevIoT')
    args = parser.parse_args()

    hostname = socket.gethostname() # get computer name
    deviot_url = "deviot.cisco.com" if args.deviot_server is None else args.deviot_server
    mqtt_url = "deviot.cisco.com:18883" if args.mqtt_server is None else args.mqtt_server
    gateway = Gateway(name='ps_' + hostname.lower(), deviot_server=deviot_url, connector_server=mqtt_url, account=args.account)
    gateway.load('things.json', 'things')
    gateway.start()

    while True:
        time.sleep(1)
        try:
            for instance in gateway.things.values():
                if getattr(instance, 'update_state', None):
                    instance.update_state()
        except:
            traceback.print_exc()
            break

    gateway.stop()
