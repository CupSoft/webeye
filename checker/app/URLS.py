from app.settings import settings as s

URL_BASE = f"{s().API_HOST}:{s().API_PORT}/api/"
URL_GET_JWT = f"{URL_BASE}auth/login/access-token/"
URL_TASKS = f"{URL_BASE}checks/"
URL_SEND_ANSWER = f"{URL_BASE}checks/results/"
