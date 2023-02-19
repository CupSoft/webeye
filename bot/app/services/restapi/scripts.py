from app.db.db_user.user_func import User


async def get_headers(tg_id: int = None) -> dict:
    headers = {"X-Requested-With": "XMLHttpRequest", "Content-Type": "application/json"}
    if tg_id is not None:
        headers["Authorization"] = f"Bearer {await User.get_jwt(tg_id)}"
    return headers
