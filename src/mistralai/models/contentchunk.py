"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel
import pydantic
from typing import Final, Optional, TypedDict
from typing_extensions import Annotated


class ContentChunkTypedDict(TypedDict):
    text: str
    

class ContentChunk(BaseModel):
    text: str
    TYPE: Annotated[Final[Optional[str]], pydantic.Field(alias="type")] = "text" # type: ignore
    
