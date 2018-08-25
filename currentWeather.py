import APIconnect
import urllib, json
import urllib.request


"""
-----------------------------------------------------------------------------------------------
PROGRAM: currentWeather.py
Author: Adam McMurchie
Summary: This program is designed to pull current weather data from openweatermap API.
Transactions are only fired once per minute to prevent abuse of the free service and
ensure that any interface built does not get blocked.

PROGRAM FLOW:

1. Import APIconnect program locally so that API key is used with calls

2. Create and maintain a 'last transaction log file' which captures the date/time of last transaction and the transaction made

3. Check logfile, if last transaction date > 1 minute, proceed with transaction else terminate program

4. Get current weather function triggered to pull current weather for all selected cities

5. Selected cities are pulled from a city.list.json file that is provided by openweathermap, as they advise.

"""


selectedCity = "2648110"
# Define the full URL with connecton key to allow transactions
URL = "http://api.openweathermap.org/data/2.5/weather?id=" + selectedCity + "&APPID=" + APIconnect.URLkey
#URL = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=" + APIconnect.URLkey


with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())



print(data.id)







#api.openweathermap.org/data/2.5/weather?q=London&APPID=fa3fb62ea1a99d5b8454e9fe3fc05a9a