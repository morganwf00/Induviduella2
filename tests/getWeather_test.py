from weather import getWeather
def test_getWeather():
    data = getWeather(59.33, 18.07)
    print(data.keys())
    print(data["daily"])
    
def test_assert():
    data = getWeather(59.33, 18.07)
    assert "daily" in data
    assert 'current' in data
    assert len(data['daily']['time']) == 3