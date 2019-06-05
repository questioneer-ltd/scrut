"""Type stubs for _pytest._code."""

# This class actually has more functions than are specified here.
# We don't use these features, so I don't think its worth including
# them in our type stub. We can always change it later.
class ExceptionInfo:
    @property
    def value(self) -> Exception: ...