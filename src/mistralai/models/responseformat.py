"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .responseformats import ResponseFormats
from mistralai.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ResponseFormatTypedDict(TypedDict):
    type: NotRequired[ResponseFormats]
    r"""An object specifying the format that the model must output. Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which guarantees the message the model generates is in JSON. When using JSON mode you MUST also instruct the model to produce JSON yourself with a system or a user message."""


class ResponseFormat(BaseModel):
    type: Optional[ResponseFormats] = None
    r"""An object specifying the format that the model must output. Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which guarantees the message the model generates is in JSON. When using JSON mode you MUST also instruct the model to produce JSON yourself with a system or a user message."""
