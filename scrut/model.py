"""Validation Model Class."""

from typing import Type, TypeVar

from pydantic import Extra
from pydantic.dataclasses import dataclass

from .source import Source

T = TypeVar("T", bound='Model')


@dataclass
class Model:
    """Validation Model."""

    class Config:
        """Configuration for pydantic."""

        extra = Extra.forbid
        validate_assignment = True

    @classmethod
    def load(cls: Type[T], source: Source) -> T:
        """Load a model from a file."""
        return cls(**source.get_data())
