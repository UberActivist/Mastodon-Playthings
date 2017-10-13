from mastodon import Mastodon
import threading, time, json, xkcd

mastodon = Mastodon(
    client_id = 'key.secret',
    access_token = 'access.secret',
    api_base_url = 'https://botsin.space'
)

def update_and_save(data):
    with open("data.json", "w") as data2:
        print("Pushing update to local file.")
        json.dump(data, data2)

def xkcd_loop():
    print("Checking for new xkcd")
    with open("data.json", "r") as data:
        stuff = json.load(data)
        if xkcd.get_latest_id() > stuff["xkcd"]["last_comic_seen"]:
            print("New comic found, tooting...")
            new_comic = xkcd.get_comic(stuff["xkcd"]["last_comic_seen"] + 1)
            status = "xkcd {} was just found...\n{}\nLink: https://xkcd.com/{}".format(str(new_comic["num"]), new_comic["title"], str(new_comic["num"]))
            mastodon.status_post(status)
            print("Toot sent")
            stuff["xkcd"]["last_comic_seen"] += 1
            update_and_save(stuff)
            if stuff["xkcd"]["last_comic_seen"] == xkcd.get_latest_id():
                print("Latest comic has been posted. Delaying check for 1 hour.")
                time.sleep(3600)
            else:
                print("We appear to be behind on comics. Checking again in 60 seconds to prevent flooding.")
                time.sleep(60)
        else:
            print("No new comic found. Checking again in 60 seconds.")
            time.sleep(60)
    xkcd_loop()

threading.Thread(target=xkcd_loop).start()
