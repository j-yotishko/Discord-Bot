import discord
import os
import requests
import json
from keep_alive import keep_alive

client= discord.Client()


def get_quote():
  response=requests.get("http://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] + " -"+json_data[0]['a']
  return(quote)


@client.event
  
async def on_read():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Heyy!")

    if message.content.startswith("$inspire"):
        quote=get_quote()
        await message.channel.send(quote)
    
keep_alive()
client.run(os.getenv('TOKEN'))


