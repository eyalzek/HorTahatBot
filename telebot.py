# telepot API: https://github.com/nickoala/telepot
import time
import re
import random
import requests
import telepot
from pprint import pprint


def get_token(secret_path):
    with open(secret_path) as f:
        return f.read().strip()


# thinking about letting it send a random gif instead of a string, or alternate between the two.
def get_gif():
    r = requests.get("http://api.giphy.com/v1/gifs/search?q=nice&api_key=dc6zaTOxFJmzC")
    gif_url = random.choice(r.json()["data"])["images"]["original"]["url"]


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance2(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    try:
        if re.match(ur"[\u05e0]+[\u05d9]{2,}[\u05e1]", msg["text"]) or "nice" in msg["text"].lower():
            # bot.sendMessage(chat_id, "Fuck you %s!" % msg["from"]["first_name"])
            bot.sendMessage(chat_id, u"\u05e0\u05d9\u05d9\u05e1\u05e1\u05e1\u05e1\u05e1\u05e1\u05e1\u05e1")
        if re.match("^[Dd][Aa][Nn]$", msg["text"]) or u"\u05d3\u05df" in msg["text"]:
            bot.sendMessage(chat_id, u"\u05d3\u05df \u05d2\u05d9\u05d9")
    except KeyError, e:
        print(e)


bot = telepot.Bot(get_token(".telegram_bot_secret"))
bot.notifyOnMessage(handle)
while True:
    time.sleep(10)