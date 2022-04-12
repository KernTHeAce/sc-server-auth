from typing import Optional
import jwt
from pydantic.class_validators import validator
from pydantic import BaseModel
from fastapi import HTTPException

from server import constants as cnt
from config import params


def _validate_token(value):
    try:
        with open(params[cnt.PUBLIC_KEY_PATH], 'rb') as file:
            public_key = file.read()
            jwt.decode(value, public_key,
                       issuer=params[cnt.ISSUER],
                       algorithm='RS256')
    except (jwt.exceptions.InvalidTokenError,
            jwt.exceptions.InvalidSignatureError,
            jwt.exceptions.InvalidIssuerError,
            jwt.exceptions.ExpiredSignatureError,
            FileNotFoundError):
        raise HTTPException(status_code=403, detail=params[cnt.MSG_ACCESS_DENIED])
    return value


class TokenModel(BaseModel):
    token: str
    token_type: Optional[str] = None
    expires_in: Optional[str] = None

    @validator("token")
    def validate_token(cls, value):
        return _validate_token(value)


class CredentialsModel(BaseModel):
    name: str
    password: str


class UserModel(BaseModel):
    access_token: str
    name: str

    @validator("access_token")
    def validate_token(cls, value):
        return _validate_token(value)


class CreateUserModel(UserModel):
    password: str
    template: str
    args: dict


class ResponseModel(BaseModel):
    msg_code: str
    msg_text: Optional[str] = None


class GetTokensResponseModel(ResponseModel):
    access_token: TokenModel
    refresh_token: TokenModel


class GetAccessTokenResponseModel(ResponseModel):
    access_token: TokenModel
