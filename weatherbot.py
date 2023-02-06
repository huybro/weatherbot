import os
import discord
import json
import requests
from weather import *
from picture import *
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
api_key = os.getenv("API")
intents = discord.Intents.default()
intents.message_content = True
command_prefix = "weather."
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_prefix):
        location = message.content.replace(command_prefix,"").lower()
        if len(location) >= 1:
            url_coordinate = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api_key}"
            coordinate = json.loads(requests.get(url_coordinate).content)
            coordinatate_data = coordinate[0]
            lat = coordinatate_data["lat"]
            lon = coordinatate_data["lon"]
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
            try:
                data = json.loads(requests.get(url).content)
                data = parse_data(data)
                await message.channel.send(embed=weather_message(data,location))
            except KeyError:
                await message.channel.send(embed=error_message(location))
    if message.content.startswith("picture."):
        try:
            description = message.content.replace("picture.","").lower()
            picture_url = create_image(description)
            await message.channel.send(picture_url)
        except:
            await message.channel.send("Can not find a picture you request")
    
        
client.run(token)



