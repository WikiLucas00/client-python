"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from mistralai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from mistralai.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Literal, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


QueryParamStatus = Literal["QUEUED", "STARTED", "VALIDATING", "VALIDATED", "RUNNING", "FAILED_VALIDATION", "FAILED", "SUCCESS", "CANCELLED", "CANCELLATION_REQUESTED"]
r"""The current job state to filter on. When set, the other results are not displayed."""

class JobsAPIRoutesFineTuningGetFineTuningJobsRequestTypedDict(TypedDict):
    page: NotRequired[int]
    r"""The page number of the results to be returned."""
    page_size: NotRequired[int]
    r"""The number of items to return per page."""
    model: NotRequired[Nullable[str]]
    r"""The model name used for fine-tuning to filter on. When set, the other results are not displayed."""
    created_after: NotRequired[Nullable[datetime]]
    r"""The date/time to filter on. When set, the results for previous creation times are not displayed."""
    created_by_me: NotRequired[bool]
    r"""When set, only return results for jobs created by the API caller. Other results are not displayed."""
    status: NotRequired[Nullable[QueryParamStatus]]
    r"""The current job state to filter on. When set, the other results are not displayed."""
    wandb_project: NotRequired[Nullable[str]]
    r"""The Weights and Biases project to filter on. When set, the other results are not displayed."""
    wandb_name: NotRequired[Nullable[str]]
    r"""The Weight and Biases run name to filter on. When set, the other results are not displayed."""
    suffix: NotRequired[Nullable[str]]
    r"""The model suffix to filter on. When set, the other results are not displayed."""
    

class JobsAPIRoutesFineTuningGetFineTuningJobsRequest(BaseModel):
    page: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""The page number of the results to be returned."""
    page_size: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 100
    r"""The number of items to return per page."""
    model: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The model name used for fine-tuning to filter on. When set, the other results are not displayed."""
    created_after: Annotated[OptionalNullable[datetime], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The date/time to filter on. When set, the results for previous creation times are not displayed."""
    created_by_me: Annotated[Optional[bool], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = False
    r"""When set, only return results for jobs created by the API caller. Other results are not displayed."""
    status: Annotated[OptionalNullable[QueryParamStatus], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The current job state to filter on. When set, the other results are not displayed."""
    wandb_project: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The Weights and Biases project to filter on. When set, the other results are not displayed."""
    wandb_name: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The Weight and Biases run name to filter on. When set, the other results are not displayed."""
    suffix: Annotated[OptionalNullable[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = UNSET
    r"""The model suffix to filter on. When set, the other results are not displayed."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["page", "page_size", "model", "created_after", "created_by_me", "status", "wandb_project", "wandb_name", "suffix"]
        nullable_fields = ["model", "created_after", "status", "wandb_project", "wandb_name", "suffix"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
