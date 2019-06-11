"""Test the model class."""
from typing import Any, Dict

import pytest
from pydantic.dataclasses import dataclass
from pydantic.error_wrappers import ValidationError

from scrut import Config, Model, Source


def test_model_instantiation() -> None:
    """Test that a plain Model can be used."""
    Model()


def test_model_with_bad_attr() -> None:
    """Test that an error occurs when using model with an unknown attribute."""
    with pytest.raises(TypeError):
        Model(bees=False)  # type: ignore

    m = Model()
    with pytest.raises(AttributeError):
        m.bees  # type: ignore

    with pytest.raises(KeyError):
        m.bees = 3  # type: ignore


# See: https://github.com/python/mypy/issues/5406
@dataclass(config=Config)  # type: ignore
class SimpleModel(Model):
    """A simple model for testing."""

    truthy: int


def test_simple_instantiation() -> None:
    """Test that SimpleModel instantiates properly."""
    s = SimpleModel(truthy=1)
    assert s.truthy == 1


def test_no_args_simple() -> None:
    """Test that we have to provide arguments."""
    with pytest.raises(TypeError):
        SimpleModel()  # type: ignore


def test_simple_usage() -> None:
    """Test that we can actually use this."""
    s = SimpleModel(truthy=1)

    assert s.truthy == 1
    s.truthy = 5
    assert s.truthy == 5


def test_simple_types() -> None:
    """Test that SimpleModel gets upset on type problems."""
    with pytest.raises(ValidationError):
        SimpleModel(truthy="notanint")  # type: ignore

    with pytest.raises(ValidationError):
        s = SimpleModel(truthy=1)
        s.truthy = "oof"  # type: ignore

    with pytest.raises(KeyError):
        s = SimpleModel(truthy=1)
        s.bees = 14  # type: ignore


class MockSource(Source):
    """A mock data source."""

    def get_data(self) -> Dict[Any, Any]:
        """Get data."""
        return {
            'truthy': 14,
        }


def test_load_simple() -> None:
    """Test the loading function."""
    ms = MockSource()

    m = SimpleModel.load(ms)

    assert m.truthy == 14
