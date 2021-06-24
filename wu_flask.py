from flask import Flask, render_template,url_for
from bs4 import BeautifulSoup
import requests
import WundergroundScraper as ws

ws_scraper = ws.Scraper("https://www.wunderground.com/dashboard/pws/KNEOMAHA130")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/v0/update', methods=['GET'])
def update_weather():
    ws_scraper.update_weather()
    return '''<h1>Underground Weather Scraper</h1>
<p>Weather Values Updated.</p>
''' 

@app.route('/api/v0/get_temp', methods=['GET'])
def get_temp():
    return {
        "Main Temperature": ws_scraper.get_temp(),
        "Unit": "Fahrenheit",
    }

@app.route('/api/v0/get_feels_like_temp', methods=['GET'])
def get_feels_like_temp():
    return {
        "Feels Like Temperature": ws_scraper.get_feels_like_temp(),
        "Unit": "Fahrenheit",
    }

@app.route('/api/v0/get_pressure', methods=['GET'])
def get_pressure():
    return {
        "Pressure": ws_scraper.get_pressure(),
        "Unit": "inHg",
    }

@app.route('/api/v0/get_dewpoint', methods=['GET'])
def get_dewpoint():
    return {
        "Dewpoint": ws_scraper.get_dewpoint(),
        "Unit": "Fahrenheit",
    }

@app.route('/api/v0/get_humidity', methods=['GET'])
def get_humidity():
    return {
        "Humidity": ws_scraper.get_humidity(),
        "Unit": "Percent",
    }

@app.route('/api/v0/get_precipitation_rate', methods=['GET'])
def get_precipitation_rate():
    return {
        "Precipitation Rate": ws_scraper.get_precipitation_rate(),
        "Unit": "Inches Per Hour",
    }

@app.route('/api/v0/get_precipitation_accumulation', methods=['GET'])
def get_precipitation_accumulation():
    return {
        "Precipitation Accumulation": ws_scraper.get_precipitation_accumulation(),
        "Unit": "Inches",
    }

@app.route('/api/v0/get_precipitation_total', methods=['GET'])
def get_precipitation_total():
    return {
            "Precipitation Total": ws_scraper.get_precipitation_total(),
            "Unit": "Inches",
    }