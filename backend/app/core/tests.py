import requests

url = "https://api.webeye.cupsoft.ru"

# creds = {"email": "user@example.com", "password": "string"}

# response = requests.post(f"{url}/auth/users", json=creds)

# creds = {"email": "admin@example.com", "password": "aboba"}

# response = requests.post(f"{url}/auth/users", json=creds)

# creds = {"username": "user@example.com", "password": "string"}

# response = requests.post(f"{url}/auth/login/access-token", data=creds)

# res_dict = response.json()

# token = res_dict["access_token"]

creds = {"username": "admin@example.com", "password": "aboba"}
response = requests.post(f"{url}/auth/login/access-token", data=creds)

res_dict = response.json()

admin_token = res_dict["access_token"]

headers = {"Authorization": f"Bearer {admin_token}"}

response = requests.get(f"{url}/auth/users/", headers=headers)

print(response.text)
