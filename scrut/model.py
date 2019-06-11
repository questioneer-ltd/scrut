"""Validation Model Class."""

from typing import TYPE_CHECKING, Type, TypeVar

from pydantic import BaseConfig, Extra

from .source import Source

if TYPE_CHECKING:
    from dataclasses import dataclass  # pragma: nocover
else:
    from pydantic.dataclasses import dataclass

T = TypeVar("T", bound='Model')


class Config(BaseConfig):
    """Configuration for pydantic."""

    extra = Extra.forbid
    validate_all = True
    validate_assignment = True


# See: https://github.com/python/mypy/issues/5406
@dataclass(config=Config)  # type: ignore
class Model:
    """Validation Model."""

    @classmethod
    def load(cls: Type[T], source: Source) -> T:
        """Load a model from a file."""
        return cls(**source.get_data())  # type: ignore
