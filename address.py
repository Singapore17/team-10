import requests

def address(locationA, locationB):

	locationA = 'Singapore ' + locationA
	locationB = 'Singapore ' + locationB

	token = 'AIzaSyDt1sdk_E9Xiauy2xb2V7otwS2qp-2xvfs'

	api = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

	payload = {
		'origins': 'Singapore 550147',
		'destinations': 'Singapore 822104',
		'mode': 'walking',
		'key': token
	}

	response = requests.get(api, params=payload)

	distance_result = response.text

	

