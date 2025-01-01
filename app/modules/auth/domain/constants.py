from enum import Enum


class AuthenticationErrors(str, Enum):
    INVALID_LOGIN = "Invalid credentials"
    INVALID_PASSWORD = "Incorrect Password"


class PasswordActions(str, Enum):
    NEW_PASSWORD = "new_password"
    CHANGE_PASSWORD = "change_password"
