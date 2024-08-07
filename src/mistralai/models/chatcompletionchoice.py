"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assistantmessage import AssistantMessage, AssistantMessageTypedDict
from mistralai.types import BaseModel
from typing import Literal, Optional, TypedDict
from typing_extensions import NotRequired


FinishReason = Literal["stop", "length", "model_length", "error", "tool_calls"]

class ChatCompletionChoiceTypedDict(TypedDict):
    index: int
    finish_reason: FinishReason
    message: NotRequired[AssistantMessageTypedDict]
    

class ChatCompletionChoice(BaseModel):
    index: int
    finish_reason: FinishReason
    message: Optional[AssistantMessage] = None
    
