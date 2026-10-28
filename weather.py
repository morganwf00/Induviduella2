import requests

APIURL = "https://api.open-meteo.com/v1/forecast"

#Request catcher to rule out http from app.py
class WeatherError(Exception):
    pass

#Get waethr for latlon city return dict(json)
def getWeather(lat: float, lon: float) -> dict[str, str | float |int]:
    # Values for request to use in the api GET
    arg: dict[str, str | float |int] = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "forecast_days": 3
    }
    try:
        # try to pull the data from the api with given argumeants
        svar = requests.get(APIURL, params=arg, timeout=5)
        svar.raise_for_status() # raise error if bad response
        return svar.json() # return the json data frim the api as dict
        
    except requests.RequestException as e:
        raise WeatherError("Forcast data unavalible") from e
        
        #return render_template("error.html", e=e), 502
    