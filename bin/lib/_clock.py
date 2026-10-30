"""Small, dependency-free time helpers.

Every function accepts an optional ``moment`` so callers (and tests) can work
against a fixed point in time instead of reading the wall clock again.
"""

from __future__ import annotations

import datetime as _dt

DEFAULT_FORMAT = "%H:%M:%S"


def now(*, utc: bool = False) -> _dt.datetime:
    """Return the current time (local by default, UTC when ``utc`` is true)."""
    if utc:
        return _dt.datetime.now(_dt.timezone.utc)
    return _dt.datetime.now()


def hour(moment: _dt.datetime | None = None) -> int:
    """Current hour (0-23)."""
    return (moment if moment is not None else now()).hour


def minute(moment: _dt.datetime | None = None) -> int:
    """Current minute (0-59)."""
    return (moment if moment is not None else now()).minute


def mint(moment: _dt.datetime | None = None) -> int:
    """Deprecated alias for :func:`minute`, kept so old callers keep working."""
    return minute(moment)


def sec(moment: _dt.datetime | None = None) -> int:
    """Current second (0-59)."""
    return (moment if moment is not None else now()).second


def timestamp(fmt: str = DEFAULT_FORMAT, moment: _dt.datetime | None = None) -> str:
    """Format a single moment in time using an ``strftime`` pattern.

    A single snapshot is taken, so the result can never mix seconds from one
    tick with seconds from the next one.
    """
    return (moment if moment is not None else now()).strftime(fmt)
