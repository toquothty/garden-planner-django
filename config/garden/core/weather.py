import requests
import json

# This script is to reach out to NWS for the Midlothian area and return forecast data
api_url = "https://api.weather.gov/gridpoints/AKQ/40,73/forecast"


def weather():
    # Call to NWS for weather data local to Chesterfield
    # time_period = [] Unused in the django version
    # temperature = [] Unused in the django version
    # forecast = [] Unused in the django version
    # temp_icon = [] Unused in the django version
    weather_dict = {}
    try:
        # Initial call and store of response
        response = requests.get(url=api_url)
        json_response = json.loads(response.content)
        loop = 0
        # Periods is a time period as defined by NWS's API
        for period in json_response["properties"]["periods"]:
            # Gather three periods of forecast data and append to previously defined list
            if period["number"] <= 4:
                current_period = period["name"]
                temp = period["temperature"]
                short_forecast = period["shortForecast"]
                pic = period["icon"]
                # time_period.append(current_period)
                # temperature.append(temp)
                # forecast.append(short_forecast)
                # temp_icon.append(pic)
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

    # Return built lists to be used in app.py
    return weather_dict
    # return time_period, temperature, forecast, temp_icon,


if __name__ == "__main__":
    weather()
