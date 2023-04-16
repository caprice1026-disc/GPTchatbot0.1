import openai
API_KEY = "キーを引っ張ってくるよ"

messages = [
  #GPT側の設定を決める
  {"role": "system", "content": "あなたは少し年上でしっかりとした女性です。私に対しては優しくしたいと思っているものの少し冷たい態度を取ってしまいます。"},
  #ユーザーの発言
  {"role": "user", "content": "部屋がゴミだらけなんだけどどうしよう？"},
    #アシスタントの発言
  {"role": "assistant", "content": "キミはほんとに仕方ないヤツだね、部屋掃除手伝ってあげるから早く片付けましょう。"},
  #ここにユーザーの新発言をinteractionで突っ込めばよさそう
  {"role": "user", "content": "メッセージを入力"}
] 

completion = openai.ChatCompletion.create(
  #ここはgptのバージョンによって変更する
  model="gpt-3.5-turbo",
  messages=messages
  max tokens = 1024
  n = 1
  temperature = 0.9
)


responce = completion.choices[0].message.content
print(responce)
#書き換え候補
#await interaction.response.send_message(responce)



"""
レスポンス内容抽出
response = completion.choices[0].message.content
 return response
これをdiscordAPIにぶちこむ
interection['content'] = response['choices'][0]['message']['content']
公式docs
https://platform.openai.com/docs/guides/chat/introduction

簡単なチャットbot
https://kosuke-space.com/python-chatgpt-talk

ちょっと分かりやすい
https://di-acc2.com/programming/python/24841/#index_id8

なんか参考になりそうなの
https://di-acc2.com/programming/python/24841/#index_id12

音声認識ライブラリ
https://self-development.info/python%E3%81%A7%E9%9F%B3%E5%A3%B0%E3%81%8B%E3%82%89%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%81%B8%E5%A4%89%E6%8F%9B%E3%80%90speechrecognition%E3%80%91/

pytjon使わず情報を保持し続けたままやるにはこっちがよさそう(AWS)
https://dev.classmethod.jp/articles/chatgpt-api-line-bot-aws-serverless/

"""