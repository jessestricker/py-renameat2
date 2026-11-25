from cffi import FFI

CDEF = """
#define RENAME_EXCHANGE ...
#define RENAME_NOREPLACE ...
#define RENAME_WHITEOUT ...
#define AT_FDCWD ...

int renameat2(int olddirfd, const char *oldpath,
    int newdirfd, const char *newpath, unsigned int flags);
"""

SRC = """
#include <fcntl.h>
#include <stdio.h>
"""

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source("_renameat2", SRC)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
