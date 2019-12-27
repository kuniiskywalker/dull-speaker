import requests
import json

def get_bot_message(message):
    api = "https://kingyobot.herokuapp.com/talk?message={message}"

    url = api.format(message=message)
    r = requests.get(url)

    data = json.loads(r.text)
    return data['message']
