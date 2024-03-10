import discord
import os
from googletrans import Translator
from dotenv.main import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

languages = {
    "🇮🇳": 'hi',
    "🇦🇷": 'es',
    "🇦🇺": 'en',
    "🇧🇩": 'bn',
    "🇧🇷": 'pt',
    "🇨🇦": 'en',
    "🇨🇳": 'zh-CN',
    "🇨🇿": 'cs',
    "🇭🇷": 'hr',
    "🇵🇱": 'pl',
    "🇷🇴": 'ro',
    "🇷🇺": 'ru',
    "🇸🇰": 'sk',
    "🇹🇷": 'tr',
    "🇬🇧": 'en',
    "🇺🇸": 'en',
    "🇫🇷": 'fr',
    "🇩🇪": 'de',
    "🇪🇸": 'es',
    "🇳🇱": 'nl',
    "🇮🇹": 'it',
    "🇬🇦": 'ga',
    "🇵🇹": 'pt',
    "🇳🇵": 'ne',
    "🇸🇷": 'sr',
    "🇺🇦": 'uk',
    "🇻🇳": 'vi',
    "🇮🇩": 'id',
    "🇵🇭": 'tl',
    "🇯🇵": 'ja',
    "🇭🇺": 'hu',
    "🇮🇸": 'is',
    "🇫🇮": 'fi',
    "🇧🇼": 'et',
    "🇧🇬": 'bg',
    "🇮🇱": 'he',
    "🇰🇷": 'ko',
    "🇱🇻": 'lv',
    "🇱🇧": 'lb',
    "🇺🇿": 'uz',
    "🇸🇦": 'ar',
    "🇿🇦": 'af'
}

@client.event
async def on_ready():
    print("We logged in as{0.user}".format(client))

@client.event
async def on_reaction_add(reaction,user):
    if reaction.emoji:
        reactedEmoji = reaction.emoji
        if not(languages.get(reactedEmoji)):
            await reaction.message.channel.send("Language not added!")
        else:
            selectedLanguage = languages.get(reactedEmoji)
            sentMessage = str(reaction.message.content)
            translater = Translator()
            sentMessage = translater.translate(sentMessage, dest=selectedLanguage).text
            await reaction.message.channel.send(sentMessage)

load_dotenv()
token = os.getenv("TOKEN")
client.run(token)