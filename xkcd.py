import requests

def get_latest_id():
    r = requests.get("https://xkcd.com/info.0.json")
    content = r.json()
    return content["num"]

def get_latest_comic():
    r = requests.get("https://xkcd.com/info.0.json")
    return r.json()

def get_comic(id):
    r = requests.get("https://xkcd.com/{}/info.0.json".format(str(id)))
    return r.json()
