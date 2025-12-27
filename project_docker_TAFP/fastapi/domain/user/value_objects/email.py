"""メールアドレスの値オブジェクト"""

from pydantic import BaseModel, ConfigDict, field_validator, model_validator, EmailStr
from typing import Any


class UserEmail(BaseModel):
    """メールアドレスの値オブジェクト"""
    model_config = ConfigDict(frozen=True)

    value: EmailStr

    @model_validator(mode='before')
    @classmethod
    def convert_string(cls, data: Any) -> Any:
        """文字列が直接渡された場合に辞書に変換"""
        if isinstance(data, str):
            return {'value': data}
        return data

    @field_validator("value")
    @classmethod
    def validate_value(cls, value: EmailStr) -> EmailStr:
        email_str = str(value)
        if len(email_str) > 255:
            raise ValueError("メールアドレスは255文字以下でなければなりません。")
        return value

    def __str__(self) -> str:
        return str(self.value)
