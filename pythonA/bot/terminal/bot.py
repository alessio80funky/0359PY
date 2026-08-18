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

import asyncio
import os

from google import genai

from dotenv import load_dotenv

import discord

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
gemini_client = genai.Client()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"ログインしました！{self.user}")

    async def on_message(self, message):
        if message.author.bot or not message.content.strip():
            return

        print(f"Message from {message.author}: {message.content}")

        try:
            response = await asyncio.to_thread(
                gemini_client.interactions.create,
                model="gemini-3.6-flash",
                input=message.content,
            )
            output = response.output_text or "返信を生成できませんでした。"

            for start in range(0, len(output), 2000):
                await message.channel.send(output[start:start + 2000])
        except Exception as error:
            print("エラー：", error)
            await message.channel.send("返信の生成中にエラーが発生しました。")

intents = discord.Intents.default()
intents.message_content = True
discord_client = MyClient(intents=intents)



#client = genai.Client()

#response = client.interactions.create(
    #model="gemini-3.6-flash",
    #input="こんにちは"
#)

#print(response.output_text)

discord_client.run(TOKEN)
