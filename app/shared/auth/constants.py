from enum import Enum


class TokenTypes(str, Enum):
    API_KEY = "api_key"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class LoginMethods(str, Enum):
    JWT = "jwt"
