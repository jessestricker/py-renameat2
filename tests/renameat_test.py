from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

import renameat2


def test_rename():
    with TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        dst = Path(tmpdir) / "dst"
        src.write_text("foo")

        renameat2.rename(src, dst)

        assert not src.exists()
        assert dst.read_text() == "foo"


def test_rename_raises_when_src_missing():
    with TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        dst = Path(tmpdir) / "dst"

        with pytest.raises(OSError):
            renameat2.rename(src, dst)

        assert not src.exists()
        assert not dst.exists()


def test_rename_overwrites_dst():
    with TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        dst = Path(tmpdir) / "dst"
        src.write_text("foo")
        dst.write_text("bar")

        renameat2.rename(src, dst)

        assert not src.exists()
        assert dst.read_text() == "foo"


def test_rename_raises_when_dst_exists_and_replace_false():
    with TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "src"
        dst = Path(tmpdir) / "dst"
        src.write_text("foo")
        dst.write_text("bar")

        with pytest.raises(OSError):
            renameat2.rename(src, dst, replace=False)

        assert src.read_text() == "foo"
        assert dst.read_text() == "bar"
