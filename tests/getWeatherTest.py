from weather import getWeather
data = getWeather(59.33, 18.07)
print(data.keys())
print(data["daily"])