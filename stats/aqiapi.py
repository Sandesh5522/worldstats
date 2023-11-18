import requests
import json

def getaqi(lat, lon):
	url = "https://air-quality.p.rapidapi.com/current/airquality"
	querystring = {"lon":lon,"lat":lat}
	headers = {
		"X-RapidAPI-Key": "d2f8813734mshe9a5d8ccc415af9p1cfad5jsn8eb6f0f8588f",
		"X-RapidAPI-Host": "air-quality.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	return response.json()
# print(getaqi(18.5196,73.8553))
