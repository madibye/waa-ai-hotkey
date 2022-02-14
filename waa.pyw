import pyperclip, urllib, requests, sys

cb = pyperclip.paste()
if "https://" in cb and "waa.ai" not in cb:
    long_url = urllib.parse.quote(cb)
    r = requests.get("http://api.waa.ai/shorten?url=%s" % long_url)
    short_url = r.json()[u'data'][u'url']
    pyperclip.copy(short_url)
