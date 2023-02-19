from app.settings import settings as s

BASE_URL = f"{s().API_HOST}:{s().API_PORT}/api/"
URL_GET_JWT = f"{BASE_URL}auth/users/telegram/get_jwt/"
URL_GET_MY_RESOURCES_UUIDS = f"{BASE_URL}auth/users/me/subscriptions/"
URL_GET_RESOURCE = f"{BASE_URL}resources/"
