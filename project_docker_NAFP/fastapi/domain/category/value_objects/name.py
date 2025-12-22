from pydantic import BaseModel, ConfigDict,field_validator

class Name(BaseModel):

    """カテゴリ名の値オブジェクト"""
    model_config = ConfigDict(frozen=True)

    value: str

    @field_validator("value")
    @classmethod
    def validate_value(cls, value: str) ->str:
        if not (1 <= len(value) <= 200):
            raise ValueError("カテゴリ名は1文字以上200文字以下でなければなりません。")
        return value
    def __str__(self) -> str:
        return self.value