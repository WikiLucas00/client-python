"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .finetuneablemodel import FineTuneableModel
from .githubrepositoryout import GithubRepositoryOut, GithubRepositoryOutTypedDict
from .jobmetadataout import JobMetadataOut, JobMetadataOutTypedDict
from .trainingparameters import TrainingParameters, TrainingParametersTypedDict
from .wandbintegrationout import WandbIntegrationOut, WandbIntegrationOutTypedDict
from mistralai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Final, List, Literal, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


Status = Literal["QUEUED", "STARTED", "VALIDATING", "VALIDATED", "RUNNING", "FAILED_VALIDATION", "FAILED", "SUCCESS", "CANCELLED", "CANCELLATION_REQUESTED"]
r"""The current status of the fine-tuning job."""

class JobOutTypedDict(TypedDict):
    id: str
    r"""The ID of the job."""
    auto_start: bool
    hyperparameters: TrainingParametersTypedDict
    model: FineTuneableModel
    r"""The name of the model to fine-tune."""
    status: Status
    r"""The current status of the fine-tuning job."""
    job_type: str
    r"""The type of job (`FT` for fine-tuning)."""
    created_at: int
    r"""The UNIX timestamp (in seconds) for when the fine-tuning job was created."""
    modified_at: int
    r"""The UNIX timestamp (in seconds) for when the fine-tuning job was last modified."""
    training_files: List[str]
    r"""A list containing the IDs of uploaded files that contain training data."""
    validation_files: NotRequired[Nullable[List[str]]]
    r"""A list containing the IDs of uploaded files that contain validation data."""
    fine_tuned_model: NotRequired[Nullable[str]]
    r"""The name of the fine-tuned model that is being created. The value will be `null` if the fine-tuning job is still running."""
    suffix: NotRequired[Nullable[str]]
    r"""Optional text/code that adds more context for the model. When given a `prompt` and a `suffix` the model will fill what is between them. When `suffix` is not provided, the model will simply execute completion starting with `prompt`."""
    integrations: NotRequired[Nullable[List[WandbIntegrationOutTypedDict]]]
    r"""A list of integrations enabled for your fine-tuning job."""
    trained_tokens: NotRequired[Nullable[int]]
    r"""Total number of tokens trained."""
    repositories: NotRequired[List[GithubRepositoryOutTypedDict]]
    metadata: NotRequired[Nullable[JobMetadataOutTypedDict]]
    

class JobOut(BaseModel):
    id: str
    r"""The ID of the job."""
    auto_start: bool
    hyperparameters: TrainingParameters
    model: FineTuneableModel
    r"""The name of the model to fine-tune."""
    status: Status
    r"""The current status of the fine-tuning job."""
    job_type: str
    r"""The type of job (`FT` for fine-tuning)."""
    created_at: int
    r"""The UNIX timestamp (in seconds) for when the fine-tuning job was created."""
    modified_at: int
    r"""The UNIX timestamp (in seconds) for when the fine-tuning job was last modified."""
    training_files: List[str]
    r"""A list containing the IDs of uploaded files that contain training data."""
    validation_files: OptionalNullable[List[str]] = UNSET
    r"""A list containing the IDs of uploaded files that contain validation data."""
    OBJECT: Annotated[Final[Optional[str]], pydantic.Field(alias="object")] = "job" # type: ignore
    r"""The object type of the fine-tuning job."""
    fine_tuned_model: OptionalNullable[str] = UNSET
    r"""The name of the fine-tuned model that is being created. The value will be `null` if the fine-tuning job is still running."""
    suffix: OptionalNullable[str] = UNSET
    r"""Optional text/code that adds more context for the model. When given a `prompt` and a `suffix` the model will fill what is between them. When `suffix` is not provided, the model will simply execute completion starting with `prompt`."""
    integrations: OptionalNullable[List[WandbIntegrationOut]] = UNSET
    r"""A list of integrations enabled for your fine-tuning job."""
    trained_tokens: OptionalNullable[int] = UNSET
    r"""Total number of tokens trained."""
    repositories: Optional[List[GithubRepositoryOut]] = None
    metadata: OptionalNullable[JobMetadataOut] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["validation_files", "object", "fine_tuned_model", "suffix", "integrations", "trained_tokens", "repositories", "metadata"]
        nullable_fields = ["validation_files", "fine_tuned_model", "suffix", "integrations", "trained_tokens", "metadata"]
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
        
