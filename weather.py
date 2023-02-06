import discord


color = 0x206694

key_features = {
    'temp':"Temperature",
    "feels_like": "Feals Like",
    "temp_min": "Minimum Temperature",
    "temp_max": "Maximum Temperature"
}
def parse_data(data):
    data = data["main"]
    del data["humidity"]
    del data["pressure"]    
    if "grnd_level" in data:
        del data["grnd_level"]
    if "sea_level" in data:
        del data["sea_level"]
    return data

def weather_message(data,location):
    location = location.title()
    message = discord.Embed(title=f'{location} Weather', description=f"Here is the weather data for {location}.",color= color)
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
        )
    return message
def error_message(location):
    location = location.title()
    return discord.Embed(title="Error",description=f"There was an error finding weather data for {location}.",color=color)

