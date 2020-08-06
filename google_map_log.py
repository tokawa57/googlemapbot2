api_key = ""


import googlemaps
import pprint # list型やdict型を見やすくprintするライブラリ

key = api_key # 上記で作成したAPIキーを入れる
client = googlemaps.Client(key) #インスタンス生成

radius = 500
loc = "日吉"
keyword = "ラーメン"

geocode_result = client.geocode(loc) # 位置情報を検索
loc2 = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
#place_result = client.places_nearby(location=loc, radius=200, type='food',keyword=q) #半径200m以内のレストランの情報を取得
#place_result = client.places_nearby(location=loc, radius=radius, type='food',keyword=keyword,language = "ja")
place_result = client.places_nearby(location=loc2, radius=radius,keyword=keyword,language = "ja")

pprint.pprint(place_result)


rates = []

for i in range(len(place_result["results"])):
	rates.append({"name":place_result["results"][i]["name"],\
		"rating":place_result["results"][i]["rating"]})

rates_sorted = sorted(rates, key=lambda x:x['rating'],reverse=True)

print(loc)
print(keyword)

for i in rates_sorted:
	print(i)