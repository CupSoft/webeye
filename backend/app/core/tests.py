import requests


url = 'http://localhost:8000/api'
creds = {
    "email": "user@example.com",
    "password": "string"
}
response = requests.post(f'{url}/auth/login/access-token', json=creds)

res_dict = response.json()

token = res_dict['access_token']

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