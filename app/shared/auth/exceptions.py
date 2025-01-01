from app.shared.exceptions import ExceptionMapper, ValidationError


class IncorrectLogin(ExceptionMapper):
    pass


class UserBlockedAttemps(ExceptionMapper):
    pass


class MaxAttemps(ExceptionMapper):
    pass


class AuthTokenException(IncorrectLogin):
    pass


class TokenExpiredError(IncorrectLogin):
    pass


class InvalidTokenError(IncorrectLogin):
    pass


# OTP Exceptions
class OTPException(ValidationError):
    pass


class AuthenticationOtpExpired(OTPException):
    pass


class AuthenticationOtpNotFound(OTPException):
    pass


class AuthenticationOtpInvalid(OTPException):
    pass


class AuthenticationOtpChannelInvalid(OTPException):
    pass
