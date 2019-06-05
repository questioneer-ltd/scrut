"""Loader definitions to load from files."""

from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class Source(metaclass=ABCMeta):
    """A loadable source of data."""

    @abstractmethod
    def get_data(self) -> Dict[Any, Any]:
        """Get the data contained in this source."""
        raise NotImplementedError  # pragma: no cover
