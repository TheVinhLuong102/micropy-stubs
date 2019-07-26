# make_stub_files: Thu 25 Jul 2019 at 22:20:16

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Logger:
    def __init__(self, name: str) -> None: ...
    def _level_str(self, level: Any) -> Union[Any, str]: ...
        #   0: return l
        # ? 0: return l
        #   1: return 'LVL%s'%level
        #   1: return str
    def setLevel(self, level: Any) -> None: ...
    def isEnabledFor(self, level: Any) -> bool: ...
    def log(self, level: Any, msg: Any, *args) -> None: ...
    def debug(self, msg: Any, *args) -> None: ...
    def info(self, msg: Any, *args) -> None: ...
    def warning(self, msg: Any, *args) -> None: ...
    def error(self, msg: Any, *args) -> None: ...
    def critical(self, msg: Any, *args) -> None: ...
    def exc(self, e: Any, msg: Any, *args) -> None: ...
    def exception(self, msg: Any, *args) -> None: ...
def getLogger(name: str) -> Any: ...
    #   0: return _loggers[name]
    # ? 0: return _loggers[str]
    #   1: return l
    # ? 1: return l
def info(msg: Any, *args) -> None: ...
def debug(msg: Any, *args) -> None: ...
def basicConfig(level: Any=INFO, filename: str=None, stream: Any=None, format: Any=None) -> None: ...
