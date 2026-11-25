# py-renameat2

This Python library provides a wrapper around Linux's
[`renameat2`](https://www.mankier.com/2/rename) function.

There are two high-level functions:

```python
from renameat2 import rename, exchange

# Equivalent to os.rename(...)
rename("path/to/src", "path/to/dst")

# Raises an OSError when destination already exists.
rename("path/to/src", "path/to/dst", replace=False)

# Supports creating _whiteout_ objects on overlay filesystems.
rename("path/to/src", "path/to/dst", whiteout=True)

# Exchange two files, atomically.
exchange("path/to/src", "path/to/dst")
```

If you like, there is also a low-level wrapper around `renameat2`:

```python
from renameat2.low_level import renameat2, RENAME_NOREPLACE, AT_FDCWD

# See the man page rename(2) for more details.
renameat2(
    olddirfd=AT_FDCWD,
    oldpath=b"path/to/src",
    newdirfd=AT_FDCWD,
    newpath=b"path/to/dst",
    flags=RENAME_NOREPLACE,
)
```

## Alternatives

This library was largely inspired by
[python-renameat2](https://github.com/jordemort/python-renameat2), which seems
unmaintained. Also, it does not easily build with Nix.
