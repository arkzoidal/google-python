#!/usr/bin/python3

import requests

# Make a GET request to your website sitemap link
r = requests.get("https://www.arkzoidal.xyz/sitemap.xml")

print(r.status_code)

# If ping to your site is successful, then ping to google sitemap submission
if r.status_code == 200:
    print("You can now submit XML sitemap")
    r = requests.get("https://www.google.com/ping?sitemap=https://www.arkzoidal.xyz/sitemap.xml")
    print(r.text)
    print(r.status_code)

