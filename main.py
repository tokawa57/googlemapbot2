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


api_key = ""

import googlemaps
import pprint # list型やdict型を見やすくprintするライブラリ

key = api_key # 上記で作成したAPIキーを入れる
client = googlemaps.Client(key) #インスタンス生成



def googlemap(ss):
    s = []
    s = ss.split()
    loc = s[0]
    keyword = s[1]
    #radius = s[2]
    geocode_result = client.geocode(loc) # 位置情報を検索
    loc2 = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
    place_result = client.places_nearby(location=loc2, radius=1000,keyword=keyword,language = "ja")
    rates = []
    for i in range(len(place_result["results"])):
        rates.append({"name":place_result["results"][i]["name"],\
            "rating":place_result["results"][i]["rating"]})
    rates_sorted = sorted(rates, key=lambda x:x['rating'],reverse=True)
    mess = []
    for i in rates_sorted:
        mess.append(i["name"]+" 評価 "+str(i["rating"]))

    ans = ""
    for i in range(len(mess)):
        if i == len(mess)-1:
            ans += mess[i]
        else:
            ans += mess[i]+"\n"
        #print(ans)

    return ans




app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


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

"""

api_key = ""
import googlemaps
import pprint # list型やdict型を見やすくprintするライブラリ
key = api_key # 上記で作成したAPIキーを入れる
client = googlemaps.Client(key) #インスタンス生成


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
    ss = event.message.text
    #rating,length = googlemap(ss)
    ans = googlemap(ss)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=ans))
            #TextSendMessage(text="てすと"))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



"""
@app.route("/")
def hello_world():
    return "hello world!"

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
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)

"""