import os

from . import low_level

type StrOrBytesPath = str | bytes | os.PathLike[str] | os.PathLike[bytes]


def rename(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
    replace: bool = True,
    whiteout: bool = False,
) -> None:
    """Rename the file or directory `src` to `dst`.

    If `src_dir_fd` or `dst_dir_fd` is given,
    interpret `src` or `dst` relatively to the respecitve directory description.

    If `replace` is `True` (the default), `dst` will be replaced if it already exists.
    Set `replace` to `False` to raise an OSError instead.

    Set `whiteout` to `True` when you want to create a _whiteout_ object at `src` while renaming.
    This option only makes sense on an overlay filesystem.
    There, when renaming a file on a lower layer, it is first copied to the upper layer and then renamed.
    A whiteout object at `src` on the upper layer is required to hide the orignal `src` at the lower layer.
    The default is `False`.
    """
    if src_dir_fd is None:
        src_dir_fd = low_level.AT_FDCWD
    if dst_dir_fd is None:
        dst_dir_fd = low_level.AT_FDCWD

    flags = 0
    if not replace:
        flags |= low_level.RENAME_NOREPLACE
    if whiteout:
        flags |= low_level.RENAME_WHITEOUT

    low_level.renameat2(
        olddirfd=src_dir_fd,
        oldpath=os.fsencode(src),
        newdirfd=dst_dir_fd,
        newpath=os.fsencode(dst),
        flags=flags,
    )


def exchange(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
) -> None:
    """Exchange the files or directories `src` and `dst` atomically.

    If `src_dir_fd` or `dst_dir_fd` is given,
    interpret `src` or `dst` relatively to the respecitve directory description.
    """
    if src_dir_fd is None:
        src_dir_fd = low_level.AT_FDCWD
    if dst_dir_fd is None:
        dst_dir_fd = low_level.AT_FDCWD

    low_level.renameat2(
        olddirfd=src_dir_fd,
        oldpath=os.fsencode(src),
        newdirfd=dst_dir_fd,
        newpath=os.fsencode(dst),
        flags=low_level.RENAME_EXCHANGE,
    )
