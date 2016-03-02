#! python3
# lucky.py - Opens several Google search result

import requests, sys, bs4, webbrowser

print('Googling........') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

