import requests
import json

def getsports():
	url = "https://odds.p.rapidapi.com/v4/sports"
	querystring = {"all":"true"}
	headers = {
		"X-RapidAPI-Key": "d2f8813734mshe9a5d8ccc415af9p1cfad5jsn8eb6f0f8588f",
		"X-RapidAPI-Host": "odds.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	return response.json()
print(getsports())
