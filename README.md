# gateway-python-starter-kit

Python based gateway service starter kit for DevIoT.

This code is based on [gateway-python-SDK](https://wwwin-github.cisco.com/DevIoT/gateway-python-sdk). You need to install SDK before using this repo.

You need python 2.7 to use python SDK and starter kit.

## Getting Started
#### 0) Set up SDK package (terminal)
If python SDK is not installed, you need to install the SDK package before using this starter kit.

Clone the SDK git repository
```
git clone https://github.com/ailuropoda0/gateway-python-sdk.git
cd gateway-python-sdk
```
Install the SDK package on python 2 
```
python setup.py install
```
#### 1) Download starter kit
```
cd ../
git clone https://github.com/ailuropoda0/gateway-python-starter-kit.git
```
#### 2) Run the sample code
```
cd gateway-python-starter-kit
python main.py --account your_deviot_id@mail.domain
```
You should use '--account' argument to set account. main.py uses public [DevIoT](https://deviot.cisco.com) server as a default value. If you want to utilize your custom DevIoT server, then use '--deviot-server' and '--mqtt-server' arguments.

After running this command, there will be some logs that your gateway is registered. If there are some error logs, it means that there are some problems to connect your gateway to the DevIoT server.

## How to build your gateway
The detail of the way to build your gateway using SDK is in [DEVNET Learning Labs](https://developer.cisco.com/learning/labs?keywords=deviot).
