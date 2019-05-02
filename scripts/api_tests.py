import requests
import json
import os

# ENDPOINT = 'http://127.0.0.1:8000/auth_api/messageapp/'
# AUTH_ENDPOINT = ENDPOINT + 'token/'
# CREATE_ENDPOINT = ENDPOINT + 'create/'

ENDPOINT = 'http://127.0.0.1:8000/auth_api/accounts/'
REGISTER_ENDPOINT = ENDPOINT + 'register/'
LOGIN_ENDPOINT = ENDPOINT + 'login/'

image_path = os.path.join(os.getcwd(), 'json_image.jpeg')

json_headers = {
    'content-type': 'application/json',
}

login_data = json.dumps(
    # {'username': 'student5',
    {'username': 'student5@mail.ccsf.edu',
     'password': 'password123'}
)

register_data = json.dumps(
    {'username': 'student16',
     'email': 'student16@mail.ccsf.edu',
     'password': 'password123',
     'password_verify': 'password123'}
)

# get_response = requests.get(ENDPOINT)
# print("\nget_response:", get_response.text)

login_response = requests.post(LOGIN_ENDPOINT, data=login_data, headers=json_headers)
print("\nlogin_response:", login_response.text)

register_response = requests.post(REGISTER_ENDPOINT, data=register_data, headers=json_headers)
print("\nregister_response:", register_response.text)
# access_token = auth_response.json()['access']
# print("\naccess_token:", access_token)
# refresh_token = auth_response.json()['refresh']
# print("\nrefresh_token:", refresh_token)


# auth_headers = {
#     'content-type': 'application/json',
#     'Authorization': 'Bearer ' + access_token
# }
post_data = json.dumps(
    {'email': 'student@mail.ccsf.edu',
     'message': 'new message for testing'}
)
# post_response = requests.post(CREATE_ENDPOINT, data=post_data, headers=auth_headers)
# print("\npost_response:", post_response.text)
