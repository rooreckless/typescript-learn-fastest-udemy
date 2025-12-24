"""作成者の値オブジェクト"""

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from typing import Any


class UserCreatedBy(BaseModel):
    """作成者の値オブジェクト"""
    model_config = ConfigDict(frozen=True)

    value: str

    @model_validator(mode='before')
    @classmethod
    def convert_string(cls, data: Any) -> Any:
        """文字列が直接渡された場合に辞書に変換"""
        if isinstance(data, str):
            return {'value': data}
        return data

    @field_validator("value")
    @classmethod
    def validate_value(cls, value: str) -> str:
        if not (1 <= len(value) <= 45):
            raise ValueError("作成者は1文字以上45文字以下でなければなりません。")
        return value

    def __str__(self) -> str:
        return self.value
