# OPEN WEATHER MAP - DATA PROCESSING 


## Current weather and forecasts collection

This repo is my mini project working with OpenWeatherMap API - there are several restrictions of use, so as this project wont be making use of any premium features (for now), I will detail restrictions below as to set expectations.


* No bulk API downloads
* 60 transactions (calls) per minute
* Sign up required
* API key requried 
* API key activation takes 10 minutes 


# INSTRUCTIONS 

Link to working wiht the API can be found here [OpenWeatherCurrentData](https://openweathermap.org/current)  

Store your Keys in a **non-github** linked directory 

## How to get accurate API response 

Information below taken from openweathermap site.  

1. Do not send requests more than 1 time per 10 minutes from one device/one API key. Normally the weather is not changing so frequently.

2. Use the name of the server as api.openweathermap.org. Please never use the IP address of the server.

3. Call API by city ID instead of city name, city coordinates or zip code. In this case you get precise respond exactly for your city. The cities' IDs can be found in the following file: Cities' IDs list.

4. Free and Startup accounts have limitation of capacity and data availability. If you do not get respond from server do not try to repeat your request immediately, but only after 10 min. Also we recommend to store your previous request data. 

5. Account gets blocked for one hour if you exceed the limit, and another our for each call, then 24 hours after 4 calls ** BE CAREFUL ** 



## PROJECT 1 Current Weather Processing
```
PROGRAM: currentWeather.py  
Author: Adam McMurchie  
Summary: This program is designed to pull current weather data from openweatermap API.  
Transactions are only fired once per minute to prevent abuse of the free service and ensure that any interface built does not get blocked.
```
PROGRAM FLOW:

1. Import APIconnect program locally so that API key is used with calls

2. Create and maintain a 'last transaction log file' which captures the date/time of last transaction and the transaction made

3. Check logfile, if last transaction date > 1 minute, proceed with transaction else terminate program

4. Get current weather function triggered to pull current weather for all selected cities

5. Selected cities are pulled from a city.list.json file that is provided by openweathermap, as they advise.