
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class NeoPixel:
    def __init__(self, pin: machine.Pin.pin, n: int, bpp: Any=3, timing: Any=0) -> None: ...
    def __setitem__(self, index: Any, val: Any) -> None: ...
    def __getitem__(self, index: Any) -> Tuple[Any]: ...
    def fill(self, color: Any) -> None: ...
    def write(self) -> None: ...
