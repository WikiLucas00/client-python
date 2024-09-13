"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel
from typing import TypedDict


class UsageInfoTypedDict(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class UsageInfo(BaseModel):
    prompt_tokens: int

    completion_tokens: int

    total_tokens: int
