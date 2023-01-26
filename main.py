from flask import Flask
from requests import get

app = Flask(__name__)
SITE_NAME = 'https://roblox.com/'
CLEAN_SITE_NAME = 'roblox.com'
CURRENT_SITE_NAME = "roproxy.asynchronousai.repl.co"

SUBDOMAINS = {}
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  data = get(f'{SITE_NAME}{path}').content

   #
  data = data.replace(CLEAN_SITE_NAME.encode(), CURRENT_SITE_NAME.encode()) # change all Roblox.Com refrences to this site
  
  return data

app.run(host='0.0.0.0', port=5555)