# GPTchatbot0.1
## 自分宛てのメモ書きなので読んだところで他の人は何の役にも立たない
軽ーく書いていたのでとりあえず保存しておく
後でintegration等のコードを書き足すこと。

~~初めて使ったけどもAWS使うの難しくね？　なんか本を読め~~
#
必要な何か
・openAI APIは過去の会話履歴を保存してくれないのでDynamoDBなりなんなりに過去ログを保存しておかないといけない。

・返信が3秒以内に始まらないとdiscordのインタラクションが止まるのでそこを意識。最悪からメッセージを送るのはあり。

・~~openAI以外には課金したくない。AWSは後で勉強するとしてお手軽にできるなんかでやりたい

## 考えていたこと
・python内で過去の一個のログだけを保持　→大多数が会話する場合にまともに会話が成り立たない。LINEとか用かも

・スプレッドシートAPI使ってスプレッドシートに過去ログを保存（会話内容,会話発信者のdiscordID,会話時間）→一定時間ごとに会話内容を削除

↑ラグがひどそうだが簡単

・トークンをハードコーディングすんなマジで

## 参考
https://dev.classmethod.jp/articles/chatgpt-api-line-bot-aws-serverless/#toc-4
