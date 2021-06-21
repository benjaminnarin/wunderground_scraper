import requests
from bs4 import BeautifulSoup

class Scraper():

    # Pass in URL for Weather Station
    def __init__(self,url):
        self.url = url
        page = requests.get(url)
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.value_dict = {}

    # Get Current Temperature 
    def get_temp(self):
        if 'main_temp' in self.value_dict:
            return self.value_dict['main_temp']
        main_temp_class = self.soup.find(class_="main-temp").find()
        main_temp_value = main_temp_class.find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'main_temp':main_temp_value})
        return main_temp_value
    
    # Get Feels Like Temperature
    def get_feels_like_temp(self):
        if 'feels_like_temp' in self.value_dict:
            return self.value_dict['feels_like_temp']
        feels_like_class = self.soup.find(class_="feels-like-temp weather__header").find()
        feels_like_temp_value = feels_like_class.find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'feels_like_temp':feels_like_temp_value})
        return feels_like_temp_value
    
    # Get Pressure
    def get_pressure(self):
        if 'pressure' in self.value_dict:
            return self.value_dict['pressure']
        pressure = self.soup.find(class_="weather__header",text="PRESSURE")
        pressure_value = pressure.find_parent('div').find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'pressure':pressure_value})
        return pressure_value

    # Get Dewpoint
    def get_dewpoint(self):
        if 'dewpoint' in self.value_dict:
            return self.value_dict['dewpoint']
        dewpoint = self.soup.find(class_="weather__header",text="DEWPOINT")
        dewpoint_value = dewpoint.find_parent('div').find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'dewpoint':dewpoint_value})
        return dewpoint_value

    # Get Humidity
    def get_humidity(self):
        if 'humidity' in self.value_dict:
            return self.value_dict['humidity']
        humidity = self.soup.find(class_="weather__header",text="HUMIDITY")
        humidity_value = humidity.find_parent('div').find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'humidity':humidity_value})
        return humidity_value

    # Get Precipitation Rate
    def get_precipitation_rate(self):
        if 'precipitation_rate' in self.value_dict:
            return self.value_dict['precipitation_rate']
        precipitation_rate = self.soup.find(class_="weather__header",text="PRECIP RATE")
        precipitation_rate_value = precipitation_rate.find_parent('div').find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'precipitation_rate':precipitation_rate_value})
        return precipitation_rate_value

    # Get Precipitation Accumulation
    def get_precipitation_accumulation(self):
        if 'precipitation_accumulation' in self.value_dict:
            return self.value_dict['precipitation_accumulation']
        precipitation_accumulation = self.soup.find(class_="weather__header",text="PRECIP ACCUM")
        precipitation_accumulation_value = precipitation_accumulation.find_parent('div').find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'precipitation_accumulation':precipitation_accumulation_value})
        return precipitation_accumulation_value

    # Get Precipitation Total
    def get_precipitation_total(self):
        if 'precipitation_total' in self.value_dict:
            return self.value_dict['precipitation_total']
        precipitation_total = self.soup.find(class_="weather__header",text="PRECIP TOTAL")
        precipitation_total_value = precipitation_total.find_parent('div').find('span',class_="wu-value wu-value-to").get_text()
        self.value_dict.update({'precipitation_total':precipitation_total_value})
        return precipitation_total_value

    # Pull Updated Weather
    def update_weather(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.value_dict.clear()

