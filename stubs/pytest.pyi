"""
Type stubs for pytest.
Note that stubs are only written for the parts that we use.
Some parts taken from https://github.com/j5api/j5 under the MIT license.
"""

from typing import ContextManager, Type

from _pytest._code import ExceptionInfo

# This function actually has more arguments than are specified here.
# We don't use these features, so I don't think its worth including
# them in our type stub. We can always change it later.
def raises(exc_type: Type[Exception]) -> ContextManager[ExceptionInfo]:
    ...
