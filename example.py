import WundergroundScraper as ws

ws_scraper = ws.Scraper("https://www.wunderground.com/dashboard/pws/KNEOMAHA130")
print("Temp: "+ ws_scraper.get_temp())
print("Feels Like Temp: "+ ws_scraper.get_feels_like_temp())
print("Pressure: "+ ws_scraper.get_pressure())
print("Dewpoint: "+ ws_scraper.get_dewpoint())
print("Humidity: "+ ws_scraper.get_humidity())
print("Precipitation Rate: "+ ws_scraper.get_precipitation_rate())
print("Precipitation Accumulation: "+ ws_scraper.get_precipitation_accumulation())
print("Precipitation Total: "+ ws_scraper.get_precipitation_total())