async def api_login_user(tg_id: int, email: str, password: str):
    name = "my_name_" + email
    if password == "123":
        name = "error"
    jwt_token = "my_jwt_token"
    return name, jwt_token


async def api_delete_user(tg_id: int):
    return True
