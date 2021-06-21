# Weather Underground Scraper

Simple web scraper for getting weather from a personal Weather Underground station. 

NOTE: The Class lazily executes scraping. Initializing the class parses but doesn't find any of the values. Values are pulled the first time their method is run and afterwards will be saved in a dictionary to reduce execution time. However calling update will delete all saved values and the dictionary values will have to be regenerated.  

Supported Data
*   Main Temp
*   Feels Like Temp
*   Pressure
*   Dew Point
*   Humidity
*   Precipitation Rate
*   Precipitation Accumulation
*   Precipitation_Total   

## Example

``` python
#Import scraper
import WundergroundScraper as ws

# Instantiate Scraper 
ws_scraper = ws.Scraper("https://www.wunderground.com/dashboard/pws/KNEOMAHA130")

# Example Methods
print("Temp: "+ ws_scraper.get_temp())
print("Feels Like Temp: "+ ws_scraper.get_feels_like_temp())
print("Pressure: "+ ws_scraper.get_pressure())
print("Dewpoint: "+ ws_scraper.get_dewpoint())
print("Humidity: "+ ws_scraper.get_humidity())
print("Precipitation Rate: "+ ws_scraper.get_precipitation_rate())
print("Precipitation Accumulation: "+ ws_scraper.get_precipitation_accumulation())
print("Precipitation Total: "+ ws_scraper.get_precipitation_total())

# Update scraped values.
ws_scraper.update_weather()
```