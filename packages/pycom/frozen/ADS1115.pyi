# make_stub_files: Fri 26 Jul 2019 at 03:02:41

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class ADS1115:
    def __init__(self, i2c: Any, address: Any=73, gain: Any=0) -> None: ...
    def _write_register(self, register: Any, value: Any) -> None: ...
    def _read_register(self, register: Any) -> Any: ...
        #   0: return ustruct.unpack('>h',data)[0]
        # ? 0: return ustruct.unpack(str, data)[number]