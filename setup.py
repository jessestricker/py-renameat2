from setuptools import setup

setup(
    cffi_modules=["renameat2_build.py:ffibuilder"],
)
