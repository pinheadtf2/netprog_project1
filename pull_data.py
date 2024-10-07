import asyncio
import json
import xml.dom.minidom
from os import getenv

import aiohttp
import yaml
from dotenv import load_dotenv


async def get_weather_json(session, location):
    async with session.get('https://api.weatherapi.com/v1/current.json',
                           params={"key": getenv("KEY"),
                                   "q": location
                                   }) as response:
        if response.status != 200:
            exit(1)
        return await response.json()


async def get_weather_xml(session, location):
    async with session.get('https://api.weatherapi.com/v1/current.xml',
                           params={"key": getenv("KEY"),
                                   "q": location
                                   }) as response:
        if response.status != 200:
            exit(1)
        text = await response.text()
        return xml.dom.minidom.parseString(text)


async def main(location):
    async with aiohttp.ClientSession() as session:
        json_response = await get_weather_json(session, location)
        with open('weather.json', 'w') as jsonfile:
            json.dump(json_response, jsonfile, indent=2)
            print('Wrote to weather.json')

        xml_response = await get_weather_xml(session, location)
        with open('weather.xml', 'w') as xmlfile:
            xml_response.writexml(xmlfile, addindent="    ", newl="\n")
            print("Wrote to weather.xml")

        with open('weather.yaml', 'w') as yamlfile:
            yaml.dump(json_response, yamlfile, indent=2)
            print('Wrote to weather.yaml')


if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main("54751"))  # Menomonie
