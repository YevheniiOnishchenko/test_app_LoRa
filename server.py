#!/usr/bin/python3

import aiocoap.resource as resource
import aiocoap
import asyncio
import json
from bmp_sensors import BMP180
import argparse

argParser = argparse.ArgumentParser(description='COAP temperature server')
argParser.add_argument('--addr', type=str, default='localhost')

args = argParser.parse_args()


print('Initialization of BMP180...')
sensor = BMP180(1)
print('Sensor initialized!')

class TemperatureResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.state = "OFF"

    async def render_get(self, request):
        sensorValue = sensor.Measure()
        payload = json.dumps({
            'temperature': sensorValue.temperature,
            'pressure': sensorValue.pressure
        }).encode('utf-8')

        print(f'Get the sensor value: {payload.decode("utf-8")}')
        return aiocoap.Message(payload=payload)


def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['temperature'], TemperatureResource())

    print(f'Starting server on {args.addr}:5683')
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=(args.addr, 5683)))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
