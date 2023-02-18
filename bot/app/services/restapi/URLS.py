from app.settings import settings as s

BASE_URL = f"{s().API_HOST}:{s().API_PORT}/"
URL_GET_JWT = f"{BASE_URL}api/auth/users/telegram/get_jwt/"
