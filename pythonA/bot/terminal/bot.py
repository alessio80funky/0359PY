#for x in range(3):
    #shitsumon = input("あなた：")

    #if shitsumon == "こんにちは":
        #print("Bot: こんにちは、元気かい？")
    #elif shitsumon == "Pythonは？どう思いますか？":
        #print("Bot: Pythonはおもろい言語やと思うで")
    #eimport oslif shitsumon == "終了":
        #print("終了します")
        #break
    #else:
        #print("Bot: その質問分かれへん")

import os

from google import genai

from dotenv import load_dotenv

import discord



class MyClient(discord.Client):
    async def on_ready(self):
        print(f"ログインしました！{self.user}")
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
discord_client = MyClient(intents=intents)


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = genai.Client()

question = input("あなた：")
try:
    response = client.interactions.create(
    model="gemini-3.6-flash",
    input=question
)
    print("Bot:",response.output_text)

except Exception as error:
    print("エラー：",error)



#client = genai.Client()

#response = client.interactions.create(
    #model="gemini-3.6-flash",
    #input="こんにちは"
#)

#print(response.output_text)

discord_client.run(TOKEN)