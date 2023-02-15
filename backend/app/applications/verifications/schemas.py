from enum import Enum


class RequestType(str, Enum):
    get = 'GET'
    post = 'POST'
    patch = 'PATCH'
    delete = 'DELETE'
