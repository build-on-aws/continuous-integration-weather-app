from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# API Key for OpenWeatherMap
api_key = "<your_api_key>"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    print(api_key)
    # Get the city from user input
    city = request.form.get("city")

    # API endpoint for current weather data
    endpoint = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=imperial"

    # Making a GET request to the endpoint
    response = requests.get(endpoint)

    # Check if the request was successful
    if response.status_code == 200:
        # Loading the response data into a Python dictionary
        data = json.loads(response.text)
        temp=data['main']['temp']
        data['main']['temp']=int(temp)
        return render_template("weather.html", data=data)
    else:
        return "Could not retrieve weather data. Response status code: " + str(response.status_code)

if __name__ == "__main__":
    app.run(debug=True)
