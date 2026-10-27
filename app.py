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