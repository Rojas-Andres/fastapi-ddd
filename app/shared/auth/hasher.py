import hashlib
import secrets
from app.shared.auth.auth_class import HasherAbstract


class Hasher(HasherAbstract):
    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str):
        return cls.pwd_context.hash(password)

    @classmethod
    def generate_random_hash(
        cls,
    ):
        random_data = secrets.token_urlsafe(16)
        md5_hash = hashlib.md5()
        md5_hash.update(random_data.encode("utf-8"))
        hash_result = md5_hash.hexdigest()
        return hash_result

    @classmethod
    def get_password_hash_sha1(cls, password: str):
        sha1 = hashlib.sha1()
        sha1.update(password.encode("utf-8"))
        hash_result = sha1.hexdigest()
        return hash_result
