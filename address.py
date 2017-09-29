import requests
import json

def address(locationA, locationB):

    locationA = 'Singapore ' + str(locationA)
    locationB = 'Singapore ' + str(locationB)

    token = 'AIzaSyDt1sdk_E9Xiauy2xb2V7otwS2qp-2xvfs'

    api = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    payload = {
            'origins': locationA,
            'destinations': locationB,
            'mode': 'walking',
            'key': token
            }

    response = requests.get(api, params=payload)

    result = response.text
    json_data = json.loads(result)
    distance_value = str(json_data["rows"][0]["elements"][0]["distance"]["text"])
    distance_number = distance_value.split(' ', 1)[0]
    return distance_number




