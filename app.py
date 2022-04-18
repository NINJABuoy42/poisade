
from imp import reload
from flask import Flask, render_template
import json
import requests


app = Flask(__name__)

@app.route('/<id>')
def home(id):
    url=f"https://poisade.anvil.app/_/api/{id}"
    data=requests.get(url)
    read=json.loads(data.content)
    return render_template('index.html',data=read)
  

if __name__ == '__main__':
    
    app.run() 