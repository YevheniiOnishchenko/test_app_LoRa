#!/usr/bin/python3

import asyncio
from aiocoap import *
import argparse

argParser = argparse.ArgumentParser(description='COAP temperature client')
argParser.add_argument('--addr', type=str, default='localhost')

args = argParser.parse_args()

async def main():
    context = await Context.create_client_context()
    request = Message(code=GET, uri=f"coap://{args.addr}/temperature")

    response = await context.request(request).response
    print(f'Result: {(response.code)} : {response.payload.decode("utf-8")}')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())