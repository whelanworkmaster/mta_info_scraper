from flask import Flask, request
from scrape_url import ScrapeUrl


app = Flask(__name__)

info_url = 'https://new.mta.info/'


scraper = ScrapeUrl(info_url)


@app.route('/status')
def get_line_status():
    line = request.args.get('line')
    return scraper.get_delayed_trains(line)


@app.route('/uptime')
def get_line_uptime():
    line = request.args.get('line')
    return scraper.get_line_uptime(line)

