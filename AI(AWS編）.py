import os
import json
import openai
import boto3
import discord.ext.commands

# ハードコードしない
DISCORD_TOKEN = "your_discord_bot_token"

# ハードコードしない
openai.api_key = "your_openai_api_key"


DYNAMODB_TABLE_NAME = "lambda-apigateway"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
prefix = "/"

# Discord Botが起動した時の処理
@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()
    
@tree.commands(name="talk",description="chatbotちゃんとトークするためのコマンドです。")
@discord.app_commands.describe(text="送りたい文章を書き込んでください。")
async def talk(interaction: discord.Interaction,text: str):

 




        # OpenAIのAPIで回答を取得
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=50
        )

        # 回答を取得
        answer = response.choices[0].text.strip()

        # Discordに回答を送信
        await message.channel.send(answer)

        # DynamoDBに会話履歴を保存
        conversation = {
            "question": text,
            "answer": responser
        }
        table.put_item(Item=conversation)

# Discord Botを起動
client.run(DISCORD_TOKEN)
