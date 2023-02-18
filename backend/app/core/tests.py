import requests


url = 'http://localhost:8000'
creds = {
    "email": "user@example.com",
    "password": "string"
}
response = requests.post(f'{url}/api/auth/login/access-token', json=creds)

res_dict = response.json()

token = res_dict['access_token']

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(f'{url}/api/auth/users/', headers=headers)

print(response.text)

response = requests.get(f'{url}/api/auth/users/me', headers=headers)


print(response.text)