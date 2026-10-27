from flask import Flask, render_template, request

app = Flask(__name__)

# City list with corresponding cordinates
citiesDic = {   
    "Stockholm": (59.33, 18.07),
    "Göteborg": (57.71, 11.97),
    "Malmö": (55.61, 13.00),
    "Umeå": (63.83, 20.26),
    "Kiruna": (67.83, 20.23),
}

#Landing page to choose city
@app.route('/')
def index():
    return render_template('index.html', cities=citiesDic)

#Endpoint for forecast
@app.route('forecast')
def forcast():
    city = request.arg.get("city", "Stockholm")
    if city not in citiesDic:
        return render_template('404.html', city=city), 404
    return render_template('forecast.html', city=city)