"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .contentchunk import ContentChunk, ContentChunkTypedDict
from mistralai.types import BaseModel
from typing import List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired


UserMessageContentTypedDict = Union[str, List[ContentChunkTypedDict]]


UserMessageContent = Union[str, List[ContentChunk]]


UserMessageRole = Literal["user"]


class UserMessageTypedDict(TypedDict):
    content: UserMessageContentTypedDict
    role: NotRequired[UserMessageRole]


class UserMessage(BaseModel):
    content: UserMessageContent

    role: Optional[UserMessageRole] = "user"
