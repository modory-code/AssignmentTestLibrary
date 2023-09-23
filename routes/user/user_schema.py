from pydantic import BaseModel, validator, EmailStr
from enum import Enum

class roleEnum(str, Enum):
    ADMIN = 'admin'
    USER = 'user'

class UserCreate(BaseModel):
    id: int
    username: str
    password1: str
    password2: str
    email: EmailStr
    role: roleEnum

    # 유효성 검사
    @validator('username', 'password1', 'password2', 'email', 'role')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    @validator('password1')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('비밀번호는 최소 8자리 이상이어야 합니다.')
        if any(char.isupper() for char in v):
            raise ValueError('비밀번호는 대문자를 포함해야 합니다.')
        if any(char.islower() for char in v):
            raise ValueError('비밀번호는 소문자를 포함해야 합니다.')
        if any(char.isdigit() for char in v):
            raise ValueError('비밀번호는 숫자를 포함해야 합니다.')
        if any(char in '!@#$%^&*' for char in v):
            raise ValueError('비밀번호는 특수문자(!@#$%^&*) 중 하나 이상을 포함해야 합니다.')
        return v
    @validator('password2')
    def match_password(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v