
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def print(*value) -> None: ...
def wait(time: int) -> None: ...
class StopWatch:
    def time(self) -> number: ...
    def pause(self) -> None: ...
    def resume(self) -> None: ...
    def reset(self) -> None: ...
