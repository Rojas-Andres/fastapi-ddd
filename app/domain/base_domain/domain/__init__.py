from enum import Enum


class AuthTypes(str, Enum):
    API_KEY = "api_key"
    BASIC = "basic"
    OAUTH = "oauth"
    JWT = "jwt"


class Configuration:
    class UserValidationType(str, Enum):
        TRY_ATTEMPS = "try_attempts"
        PASSWORD_VALIDATE = "password_validate"

    class UserAuthType(str, Enum):
        TOKEN = "token"
        TWO_FA = "2fa"
