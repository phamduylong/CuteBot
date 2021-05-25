import discord
import pyjokes
import requests
import json
import random
import time
from dadjokes import Dadjoke





def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " - " + json_data[0]["a"]

    return (quote)




def get_joke():
    joke = pyjokes.get_joke()
    return (joke)
def get_dads_joke():

    dads_joke = Dadjoke()
    return (dads_joke.joke)


#sad_words = ["sad", "unhappy", "depressed", "unmotivated"]

#encouraging_starters = ["Cheer up!", "Hang in there!", "Everything is gonna be ok dear ^^ don't you worry.",
#                        "Stay strong 💪 don't give up, I got your back", "I believe in you! Keep pushing for it",
#                        "Don't ask yourself 'What if I fall?'. My dear, what if you fly?", "Be courage, always!",
#                        "It always seems impossible until it is done!",
#                       "I wish I could be there with you 😔",
#                        "Don't give up when dark times come. The more storms you face in your life, the stronger you'll be 😉"
#                        "I hope you wake up feeling exceptional. You are important, needed, and unique."
#                        "If you are still breathing maybe it is not such a bad day after all."
#                        "Life is too short for us to dwell on sadness. Cheer up and live life to the fullest."
#                        "Look around, the world has so much to offer, just live every second of your life and don’t think about the bad things."]

agreements = ["OK!", "Sure", "Who wouldn't?", "You got it", "What if I don't? Whatchu gonna do hooman?",
              "Did someone say joke? Here's one for you 😉😉", "Your wish is my command 😊😊",
              "Coming right away", "You got it boss 👌👌"]

bot_complains = ["I really am a human. I have emotions 😡 Emojis I mean", "Why wouldn't anyone believe me?",
                 "Wrong. Human soul in a bot", "Stop doubting me!!! I might be smarter than you, don't you think?"]

sad_bot = ["Okay 🤐🤐", "Did I say something wrong 😥 I'm sorry", "Fine. You know how to find me 😔",
           "I'm here to talk, but if that is what you want then be it ☹"]

client = discord.Client()





@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


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


        if (agr == "What if I don't? Whatchu gonna do hooman 😎 I'm not afraid of you"):
            await message.channel.send(agr)
            time.sleep(2)
            await message.channel.send("Nah I'm kidding hehe 😁😁. Here ya go:")
            time.sleep(1)
            await message.channel.send(quote)
        else:
            await message.channel.send(agr)
            time.sleep(1)
            await message.channel.send(quote)

#    if any(word in msg for word in sad_words) and msg.find("not") == -1 or message.content.startswith('>cheer me up') and msg.find("not") == -1:
 #       await message.channel.send(random.choice(encouraging_starters))

    if msg.startswith('/cutebot help'):
        await message.channel.send("Yo wassup human,\nI am cute bot 🥰🥰 (Actually I'm a human pretending to be a bot). Here's what I can do:\n"
                                   "1 /quote or /inspire me: I can give you an inspiring quote\n"
                                   "2 /cutebot help: Instructions to be my friend 🤭🤭\n"
                                   "3 /tell a joke or /joke: Ready for a laugh? Can't wait to tell my joke 😉😉")

    if msg.startswith('/tell a joke'):
        joke = get_joke()
        if (agr == "What if I don't? Whatchu gonna do hooman?"):
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
        if (agr == "What if I don't? Whatchu gonna do hooman 🤔 I'm not afraid of you 😎"):
            time.sleep(2)
            await message.channel.send("Nah I'm kidding hehe 😁😁. Here ya go:")
            time.sleep(1)
            await message.channel.send(dads_joke)
        else:
            await message.channel.send(agr)
            time.sleep(1)
            await message.channel.send(dads_joke)

    if msg.find('not')!=-1 and msg.find("human")!=-1:
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
        await  message.channel.send("┬─┬ ノ( ゜-゜ノ)")

    if msg.find("┬─┬ ノ( ゜-゜ノ)") != -1:
        await message.channel.send("(╯°□°）╯︵ ┻━┻")









client.run("ODIzODQxNjc5MjU3NzYzODQx.YFmsWg.sUHAeVrSPfWhNMGYCSDjxRiyTXw     ")
