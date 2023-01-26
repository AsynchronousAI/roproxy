from flask import Flask
from requests import get
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  url = request.headers.get('url')
  if url:
    args = request.headers
    # remove url from args
    args.pop('url')
    
    i = 0
    for arg in args:
      if i == 0:
        url += f"?{arg}={args[arg]}"
      else:
        url += f"&{arg}={args[arg]}"
      i += 1
    data = get(url, headers = request.headers)
  
    return data
  else:
    return "Headers missing"
app.run(host='0.0.0.0', port=5555)