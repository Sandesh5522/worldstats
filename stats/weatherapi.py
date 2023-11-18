import requests
import json

def getweather(lat,lon):
	url = "https://weatherapi-com.p.rapidapi.com/current.json"
	# try removing this
	lat = str(lat)
	lon = str(lon)
	querystring = {"q":lat+","+lon}
	# Shivajinagar coordinates for testing
	# querystring = {"q":"18.531804876008586, 73.84435927891408"}
	headers = {
		"X-RapidAPI-Key": "d2f8813734mshe9a5d8ccc415af9p1cfad5jsn8eb6f0f8588f",
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	# print(response.json())
	return response.json()
