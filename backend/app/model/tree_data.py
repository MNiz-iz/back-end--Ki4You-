from typing import Optional
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, ForeignKey


class Trees(SQLModel, table=True):
    __tablename__ = "trees"

    indexTree: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str
    another_name: str
    sci_name: str
    family: str
    type: str
    category: str
    size: str
    hieght: str
    hieght_max: int
    nature: str
    flower: str
    leaf: str
    note_nature: str
    grow_rate: str
    watering: str
    sunrise: str
    soil: str
    breed: str
    additional_care: str
    special_feature: str
    url_picture: str
    c_picture: str
    min_price: int
    max_price: int
    advice: str
    auspicious: str
    plant_detail: str
    countLike: int


class Features(SQLModel, table=True):
    __tablename__ = "features"

    indexFeatures: Optional[str] = Field(None, primary_key=True, nullable=False)
    name: str
    desc: str


class HasFeatures(SQLModel, table=True):
    __tablename__ = "hasfeatures"

    indexTree: str = Field(sa_column=Column(String, ForeignKey("trees.indexTree", ondelete="CASCADE"), nullable=False, primary_key=True))
    indexFeatures: str = Field(sa_column=Column(String, ForeignKey("features.indexFeatures", ondelete="CASCADE"), nullable=False, primary_key=True))


class Pollutions(SQLModel, table=True):
    __tablename__ = "pollutions"

    indexPollution: Optional[str] = Field(None, primary_key=True, nullable=False)
    pollution_name: str
    desc: str


class Purifies(SQLModel, table=True):
    __tablename__ = "purifies"

    indexTree: str = Field(sa_column=Column(String, ForeignKey("trees.indexTree", ondelete="CASCADE"), nullable=False, primary_key=True))
    indexPollution: str = Field(sa_column=Column(String, ForeignKey("pollutions.indexPollution", ondelete="CASCADE"), nullable=False, primary_key=True))


class ListPrices(SQLModel, table=True):
    __tablename__ = "listprices"

    indexTree: str = Field(sa_column=Column(String, ForeignKey("trees.indexTree", ondelete="CASCADE"), nullable=False, primary_key=True))
    rangePrice: Optional[str] = Field(None, primary_key=True, nullable=False)
    price: int
    url_link: str