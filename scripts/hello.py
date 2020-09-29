from flask import Flask
import requests
from urllib.request import urlopen
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/trains')
def get_mta_info():
    info_url = 'https://new.mta.info/'
    page = urlopen(info_url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
    return html

