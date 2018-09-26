import urllib.request
import time
from win10toast import ToastNotifier
import requests
import datetime
import tempfile
import update




website = 'https://us.api.battle.net/data/wow/token/?namespace=dynamic-us&locale=en_US&access_token=jnakhmxmt8rk3xna3ewqnpdw'
response = requests.get('https://us.api.battle.net/data/wow/token/?namespace=dynamic-us&locale=en_US&access_token=jnakhmxmt8rk3xna3ewqnpdw')

def check():
    response = urllib.request.urlopen(website)
    html = response.read()
    return(html)
prevhtml = check()
while True:
    newhtml = check()
    if newhtml != prevhtml:
        response = requests.get('https://us.api.battle.net/data/wow/token/?namespace=dynamic-us&locale=en_US&access_token=jnakhmxmt8rk3xna3ewqnpdw')
        price = response.text[140:146]
        ints = int(price)
        formated = (format(ints,',d'))
        toaster = ToastNotifier()
        toaster.show_toast("WoW Token",formated,icon_path="wow.ico",duration=60,threaded=True)

        print()
        print(formated)
    prevhtml = newhtml
    time.sleep(60)
