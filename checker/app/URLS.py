from app.settings import settings as s

URL_BASE = f"{s().API_HOST}:{s().API_PORT}/api/"
URL_TASKS = f"{URL_BASE}/tasks"
