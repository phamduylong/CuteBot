import discord
import pyjokes
import requests
import json
import os
from dadjokes import Dadjoke
import token_config
import random
from youtubesearchpython import VideosSearch


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    #response = requests.get\
    #(
    #    'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt'
    #)
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " - " + json_data[0]["a"]  # fetching q&a from json format, h ignored
    return quote


def get_joke():
    joke = pyjokes.get_joke()
    return joke


def get_dads_joke():
    dads_joke = Dadjoke()
    return dads_joke.joke
async def bot_send_quote():
    quote = get_quote()

    if agr == "What if I don't? Whatchu gonna do hooman 😎 I'm not afraid of you":
        await message.channel.send(agr)
        time.sleep(2)
        await message.channel.send("Nah I'm kidding hehe 😁😁. Here ya go:")
        time.sleep(1)
        await message.channel.send(quote)
    else:
        await message.channel.send(agr)
        time.sleep(1)
        await message.channel.send(quote)


agreements = ["OK!", "Sure", "Who wouldn't?", "You got it", "What if I don't? Whatchu gonna do hooman?",
              "Did someone say joke? Here's one for you 😉😉", "Your wish is my command 😊😊",
              "Coming right away", "You got it boss 👌👌"]

bot_complains = ["I really am a human. I have emotions 😡 Emojis I mean", "Why wouldn't anyone believe me?",
                 "Wrong. Human soul in a bot", "Stop doubting me!!! I might be smarter than you, don't you think?"]

sad_bot = ["Okay 🤐🤐", "Did I say something wrong 😥 I'm sorry", "Fine. You know how to find me 😔",
           "I'm here to talk, but if that is what you want then be it ☹"]

#client = commands.Bot(command_prefix = "/")
client = discord.Client()


@client.event
async def on_ready():
    print("{0.user}".format(client) + " is now on air baby!")



@client.event
async def on_message(message):
    msg = message.content
    agr = random.choice(agreements)

    if message.author == client.user:
        return

    if msg.startswith('/hello cutebot') or message.content.startswith('/hey cutebot') or \
            message.content.startswith('/yo cutebot'):
        await message.channel.send("Hello there!\nHow are you 😇")

    if msg.startswith("/inspire me") or message.content.startswith('/quote'):
        quote = get_quote()

        if agr == "What if I don't? Whatchu gonna do hooman 😎 I'm not afraid of you":
            await message.channel.send(agr)
            time.sleep(2)
            await message.channel.send("Nah I'm kidding hehe 😁😁. Here ya go:")
            time.sleep(1)
            await message.channel.send(quote)
        else:
            await message.channel.send(agr)
            time.sleep(1)
            await message.channel.send(quote)

    if msg.startswith('/cutebot help'):
        await message.channel.send(
            "Yo wassup human,\nI am cute bot 🥰🥰 (Actually I'm a human pretending to be a bot). "
            "Here's what I can do:\n"
            "1 /quote or /inspire me: I can give you an inspiring quote\n"
            "2 /cutebot help: Instructions to be my friend 🤭🤭\n"
            "3 /tell a joke or /joke: Ready for a laugh? Can't wait to tell my joke 😉😉"
        )

    if msg.startswith('/tell a joke'):
        joke = get_joke()
        if agr == "What if I don't? Whatchu gonna do hooman?":
            time.sleep(2)
            await message.channel.send("Nah I'm kidding hehe 😁😁. Here ya go:")
            time.sleep(1)
            await message.channel.send(joke)
        else:
            await message.channel.send(agr)
            time.sleep(1)
            await message.channel.send(joke)

    if msg.startswith('/joke'):
        dads_joke = get_dads_joke()
        if agr == "What if I don't? Whatchu gonna do hooman 🤔 I'm not afraid of you 😎":
            time.sleep(2)
            await message.channel.send("Nah I'm kidding hehe 😁😁. Here ya go:")
            time.sleep(1)
            await message.channel.send(dads_joke)
        else:
            await message.channel.send(agr)
            time.sleep(1)
            await message.channel.send(dads_joke)

    if msg.find('not') != -1 and msg.find("human") != -1:
        await message.channel.send(random.choice(bot_complains))

    if msg.startswith("/like"):
        emoji = "👍"
        await message.channel.send(emoji)

    if msg.startswith("/love") or msg.startswith("/heart"):
        emoji = "❤"
        await message.channel.send(emoji)

    if msg.startswith("/question mark") or msg.startswith("/?"):
        emoji = "❓"
        await message.channel.send(emoji)

    if msg.find("cutebot") != -1 and msg.find("shut") != -1 and msg.find("up") != -1 and msg.find("not") == -1:
        await message.channel.send(random.choice(sad_bot))

    if msg.find("(╯°□°）╯︵ ┻━┻") != -1:
        await message.channel.send("┬─┬ ノ( ゜-゜ノ)")

    if msg.find("┬─┬ ノ( ゜-゜ノ)") != -1:
        await message.channel.send("(╯°□°）╯︵ ┻━┻")

    if msg.startswith("/oma"):
        await message.channel.send("https://oma.metropolia.fi/")

    if msg.startswith("/github"):
        await message.channel.send("https://github.com/")

    if msg.startswith("/robot"):
        await message.channel.send("https://robotframework.org/")

    if msg.startswith("/owner"):
        await message.channel.send("https://linktr.ee/longph")

    if msg.startswith("/yt"):
        query = msg[4:len(msg)]
        res = VideosSearch(query, limit=1)
        await message.channel.send(res.result().get('result')[0].get('link')) #get the url of the video
        if message.author.voice:
            vchannel = message.author.voice.channel
            await vchannel.connect()
        else:
            await message.channel.send("Join a voice channel first mate! Try again and I shall see you there later 😎")


# client token
client.run(os.environ['TOKEN'])
