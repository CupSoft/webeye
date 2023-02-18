import requests


url = 'http://localhost:8000/api'
creds = {
    "username": "user@example.com",
    "password": "string"
}
response = requests.post(f'{url}/auth/login/access-token', data=creds)

print(response.text)
res_dict = response.json()

token = res_dict['access_token']
print(token)

creds = {
    "username": "admin@example.com",
    "password": "string"
}
response = requests.post(f'{url}/auth/login/access-token', data=creds)

res_dict = response.json()

admin_token = res_dict['access_token']


headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(f'{url}/auth/users/', headers=headers)

print(response.text)

response = requests.get(f'{url}/auth/users/me', headers=headers)

print(response.text)

response = requests.get(f'{url}/resources/', headers=headers)

print(response.text)

response = requests.get(f'{url}/resources/nodes/', headers=headers)

print(response.text)

response = requests.get(f'{url}/checks/', headers=headers)

print(response.text)

response = requests.get(f'{url}/checks/results/', headers=headers)

print(response.text)

response = requests.get(f'{url}/auth/users/telegram/generate_token', headers=headers)

print(response.text)

headers = {
    "Authorization": f"Bearer {admin_token}"
}


response = requests.post(f'{url}/auth/users/telegram/get_jwt', headers=headers,
                        json={'token': 'PrUVeeYIWmRZXDhvNmDpiwnEMFUEotlf', 'id': 1})

print(response.text)