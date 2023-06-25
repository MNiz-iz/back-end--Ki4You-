from pydantic import BaseModel
from fastapi import HTTPException
from typing import Optional, TypeVar, Generic, List
from pydantic.generics import GenericModel

T = TypeVar('T')


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None


class PageResponse(GenericModel, Generic[T]):

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[T]


class Types(BaseModel):
    types: str


class Outdoor(BaseModel):
    outdoor: int


class Indoor(BaseModel):
    indoor: int


class Semi(BaseModel):
    semi: int


class Pots(BaseModel):
    pots: int


class Garden(BaseModel):
    garden: int


class Hanging(BaseModel):
    hanging: int


class Little(BaseModel):
    little: int


class Mid(BaseModel):
    mid: int


class Freq(BaseModel):
    freq: int


class Faintly(BaseModel):
    faintly: int


class Full(BaseModel):
    full: int


class Half(BaseModel):
    half: int


class S(BaseModel):
    s_s: int


class M(BaseModel):
    s_m: int


class L(BaseModel):
    s_l: int


class Purify(BaseModel):
    purify: int


class Aus(BaseModel):
    aus: int


class Inshade(BaseModel):
    inshade: int


class Beginner(BaseModel):
    beginner: int


class Exposestosun(BaseModel):
    exposestosun: int


class Flower(BaseModel):
    flower: int

