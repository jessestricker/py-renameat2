"""A low-level wrapper around renameat2."""

import os

from _renameat2 import ffi as _ffi  # type: ignore
from _renameat2 import lib as _lib  # type: ignore

AT_FDCWD: int = _lib.AT_FDCWD  # type: ignore
RENAME_EXCHANGE: int = _lib.RENAME_EXCHANGE  # type: ignore
RENAME_NOREPLACE: int = _lib.RENAME_NOREPLACE  # type: ignore
RENAME_WHITEOUT: int = _lib.RENAME_WHITEOUT  # type: ignore


def renameat2(
    olddirfd: int,
    oldpath: bytes,
    newdirfd: int,
    newpath: bytes,
    flags: int,
) -> None:
    """Call `renameat2`.

    When `renameat2` returns a non-zero value,
    raises OSError with the current value of `errno`.
    """

    result: int = _lib.renameat2(  # type: ignore
        olddirfd,
        oldpath,
        newdirfd,
        newpath,
        flags,
    )
    errno: int = _ffi.errno  # type: ignore

    if result != 0:
        raise OSError(errno, os.strerror(errno))  # type: ignore
