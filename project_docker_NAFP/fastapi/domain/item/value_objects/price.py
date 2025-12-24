"""商品価格の値オブジェクト"""

from pydantic import BaseModel, ConfigDict, field_validator, model_validator
from typing import Any


class ItemPrice(BaseModel):
    """商品価格の値オブジェクト"""
    model_config = ConfigDict(frozen=True)

    value: int

    @model_validator(mode='before')
    @classmethod
    def convert_int(cls, data: Any) -> Any:
        """整数が直接渡された場合に辞書に変換"""
        if isinstance(data, int):
            return {'value': data}
        return data

    @field_validator("value")
    @classmethod
    def validate_value(cls, value: int) -> int:
        if value < 0:
            raise ValueError("商品価格は0以上でなければなりません。")
        return value

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
