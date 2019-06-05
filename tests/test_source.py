"""Test the Source class and related functions."""

from typing import Any, Dict

import pytest

from scrut.source import Source


def test_source_is_abstract() -> None:
    """Test that Source is an abstract class."""
    with pytest.raises(TypeError) as e:
        # Ignoring because mypy doesn't like us doing bad things in tests.
        Source()  # type: ignore
    assert "abstract" in str(e.value)


class TestSource(Source):
    """A test source that we use for testing."""

    def get_data(self) -> Dict[Any, Any]:
        """Get the data contained in this source."""
        return {}


def test_test_source_get_data() -> None:
    """Test that the test source works."""
    ts = TestSource()
    assert ts.get_data() == {}
