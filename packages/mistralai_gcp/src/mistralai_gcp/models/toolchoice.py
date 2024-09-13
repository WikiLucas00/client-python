"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .functionname import FunctionName, FunctionNameTypedDict
from .tooltypes import ToolTypes
from mistralai_gcp.types import BaseModel
from mistralai_gcp.utils import validate_open_enum
from pydantic.functional_validators import PlainValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ToolChoiceTypedDict(TypedDict):
    r"""ToolChoice is either a ToolChoiceEnum or a ToolChoice"""

    function: FunctionNameTypedDict
    r"""this restriction of `Function` is used to select a specific function to call"""
    type: NotRequired[ToolTypes]


class ToolChoice(BaseModel):
    r"""ToolChoice is either a ToolChoiceEnum or a ToolChoice"""

    function: FunctionName
    r"""this restriction of `Function` is used to select a specific function to call"""

    type: Annotated[Optional[ToolTypes], PlainValidator(validate_open_enum(False))] = (
        None
    )
