# make_stub_files: Wed 17 Jul 2019 at 02:45:28

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def try_remove(fn: str) -> None: ...
def get_filesize(fn: str) -> Any: ...
    #   0: return os.stat(fn)[6]
    # ? 0: return os.stat(str)[number]
class RotatingFileHandler(Handler):
    def __init__(self, filename: str, maxBytes: Any=0, backupCount: Any=0) -> None: ...
    def emit(self, record: Any) -> None: ...
