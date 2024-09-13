"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai_azure.types import BaseModel
from typing import TypedDict


class FunctionNameTypedDict(TypedDict):
    r"""this restriction of `Function` is used to select a specific function to call"""

    name: str


class FunctionName(BaseModel):
    r"""this restriction of `Function` is used to select a specific function to call"""

    name: str
