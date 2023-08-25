import requests
import json

# This script is to reach out to NWS for the Midlothian area and return forecast data
api_url = "https://api.weather.gov/gridpoints/AKQ/40,73/forecast"


def weather():
    weather_dict = {}
    try:
        # Initial call and store of response
        response = requests.get(url=api_url)
        json_response = json.loads(response.content)
        loop = 0
        # Periods is a time period as defined by NWS's API
        for period in json_response["properties"]["periods"]:
            # Gather four periods of forecast data and append to dictionary
            if period["number"] <= 4:
                current_period = period["name"]
                temp = period["temperature"]
                short_forecast = period["shortForecast"]
                pic = period["icon"]
                weather_dict[loop] = {
                    "time_period": current_period,
                    "temperature": temp,
                    "forecast": short_forecast,
                    "temp_icon": pic,
                }
                loop += 1

    except requests.exceptions.RequestException as err:
        print("HTTP Request failed")
        print(err)

    # Return built lists to be used in app.py, example data below
    """ {0: {'time_period': 'Today', 'temperature': 94, 'forecast': 'Isolated Rain Showers then Chance Showers And Thunderstorms', 'temp_icon': 'https://api.weather.gov/icons/land/day/rain_showers,20/tsra_sct,50?size=medium'}, 
         1: {'time_period': 'Tonight', 'temperature': 72, 'forecast': 'Chance Showers And Thunderstorms', 'temp_icon': 'https://api.weather.gov/icons/land/night/tsra_sct,50/tsra_sct,20?size=medium'}, 
         2: {'time_period': 'Saturday', 'temperature': 92, 'forecast': 'Mostly Sunny then Slight Chance Showers And Thunderstorms', 'temp_icon': 'https://api.weather.gov/icons/land/day/sct/tsra_hi,20?size=medium'}, 
         3: {'time_period': 'Saturday Night', 'temperature': 70, 'forecast': 'Chance Showers And Thunderstorms', 'temp_icon': 'https://api.weather.gov/icons/land/night/tsra_hi,30?size=medium'}} """

    return weather_dict
    # return time_period, temperature, forecast, temp_icon,


if __name__ == "__main__":
    weather()
