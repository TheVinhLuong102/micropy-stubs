# make_stub_files: Thu 25 Jul 2019 at 22:20:25

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class NeoPixel:
    def __init__(self, pin: machine.Pin.pin, n: int, bpp: Any=3, timing: Any=1) -> None: ...
    def __setitem__(self, index: Any, val: Any) -> None: ...
    def __getitem__(self, index: Any) -> Tuple[Any]: ...
    def fill(self, color: Any) -> None: ...
    def write(self) -> None: ...
