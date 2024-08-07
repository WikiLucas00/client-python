"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai_gcp.types import BaseModel
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import NotRequired


class FunctionTypedDict(TypedDict):
    name: str
    parameters: Dict[str, Any]
    description: NotRequired[str]
    

class Function(BaseModel):
    name: str
    parameters: Dict[str, Any]
    description: Optional[str] = ""
    
