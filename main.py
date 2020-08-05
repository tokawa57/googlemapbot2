from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)

import os


#heroku config:set YOUR_CHANNEL_SECRET="60307a5736b1a204d4af19ed3147523e" --app googlemapbot
#heroku config:set YOUR_CHANNEL_ACCESS_TOKEN="Kox8Y5ER51xN3QeC67g6dZtsruBXydyF6TbHSDkcAkt6tzm7TugkYJBPYv92+zJFu85tGEJ1NPhasU4VwKtKv/2yFQnAQuKrkREvlS6/MQqQo2P7FoJ4d+J4RxE7WnYFOAkzsgShNUZvUNk+bvvF1AdB04t89/1O/w1cDnyilFU=" --app googlemapbot

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


"""
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='「' + event.message.text + '」って何？')
     )

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
"""



#CS = "60307a5736b1a204d4af19ed3147523e"
#AT = "Kox8Y5ER51xN3QeC67g6dZtsruBXydyF6TbHSDkcAkt6tzm7TugkYJBPYv92+zJFu85tGEJ1NPhasU4VwKtKv/2yFQnAQuKrkREvlS6/MQqQo2P7FoJ4d+J4RxE7WnYFOAkzsgShNUZvUNk+bvvF1AdB04t89/1O/w1cDnyilFU="
#"""

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


#"""