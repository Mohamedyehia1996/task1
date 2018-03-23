from flask import Flask

import os
import facebook

graph = facebook.GraphAPI(access_token="EAACEdEose0cBAOUgTxGpdWZCBbb1IZC0ZAc3Stf8z6Fut0eTu3wcICE8thNubxNMZCFMoSev1HaWZBqLYarMtTUexvioREZCyOFu3d5XMLVKplOeww6XlGZAqyE5GuQuhGZClFus1UsqQupmzqNyZAvKViPs4yT3uPXXXShTzxZB8e2IvSbhVgnxxTxZCMAcja1ZB5x08yVVbbBfTAZDZD", version="2.10")
profile=graph.get_object('me')
posts=graph.get_connections(profile['id'],'posts',limit=25,fields="message")

for post in posts['data']:

    json_data = get_data(request.data)
    post = user_create(
    json_data["message"]["id"])

