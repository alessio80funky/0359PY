#for x in range(3):
    #shitsumon = input("あなた：")

    #if shitsumon == "こんにちは":
        #print("Bot: こんにちは、元気かい？")
    #elif shitsumon == "Pythonは？どう思いますか？":
        #print("Bot: Pythonはおもろい言語やと思うで")
    #elif shitsumon == "終了":
        #print("終了します")
        #break
    #else:
        #print("Bot: その質問分かれへん")

from google import genai

from dotenv import load_dotenv

load_dotenv()

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



client = genai.Client()

response = client.interactions.create(
    model="gemini-3.6-flash",
    input="こんにちは"
)

print(response.output_text)

