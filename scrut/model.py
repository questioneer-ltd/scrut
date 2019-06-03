"""Validation Model Class."""

from typing import TextIO, Type, TypeVar

from pydantic import Extra
from pydantic.dataclasses import dataclass

T = TypeVar("T", bound='Model')


@dataclass
class Model:
    """Validation Model."""

    class Config:
        """Configuration for pydantic."""

        extra = Extra.forbid
        validate_assignment = True

    @classmethod
    def load_from_file(cls: Type[T], fp: TextIO) -> T:
        """Load a model from a file."""

    @classmethod
    def load_from_str(cls: Type[T], data: str) -> T:
        """Load a model from a string."""
