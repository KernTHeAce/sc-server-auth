import re

from server import constants as cnt
from config import params


class BaseVerifier:
    def __init__(self, pattern: str) -> None:
        self.pattern = re.compile(pattern)

    def verify(self, string: str) -> bool:
        return bool(self.pattern.match(string))


class CredentialsVerifier(BaseVerifier):
    def verify(self, string: str) -> bool:
        return string is not None and super().verify(string)


username_verifier = CredentialsVerifier(params[cnt.USERNAME_PATTERN])
password_verifier = CredentialsVerifier(params[cnt.PASSWORD_PATTERN])
