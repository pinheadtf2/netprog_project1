import asyncio
import json
import xml.etree.ElementTree as ET

import yaml
from rich import print


async def parse_xml():
    xmldata = ET.parse("weather.xml")
    root = xmldata.getroot()
    condition_element = root.find(".//condition")
    condition = condition_element.find("text").text
    time = root.find(".//last_updated").text
    # print(f"[bold blue]XML:[/bold blue] It was [purple]{condition}[/purple] on {time}")
    return condition


async def parse_json():
    with open("weather.json") as jsonfile:
        jsondata = json.load(jsonfile)
        condition = jsondata['current']['condition']['text']
        time = jsondata['current']['last_updated']
        # print(f"[bold yellow]JSON:[/bold yellow] It was [purple]{condition}[/purple] on {time}")
        return condition


async def parse_yaml():
    with open("weather.yaml") as yamlfile:
        try:
            yamldata = yaml.safe_load(yamlfile)
            condition = yamldata['current']['condition']['text']
            time = yamldata['current']['last_updated']
            # print(f"[bold red]YAML:[/bold red] It was [purple]{condition}[/purple] on {time}")
            return condition
        except yaml.YAMLError as exc:
            print(exc)


async def main():
    await parse_xml()
    await parse_json()
    await parse_yaml()


if __name__ == '__main__':
    asyncio.run(main())
