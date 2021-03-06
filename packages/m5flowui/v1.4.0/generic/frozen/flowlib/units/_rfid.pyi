
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Rfid:
    def __init__(self, port: Any, addr: Any=40) -> None: ...
    def _available(self) -> None: ...
    def readBlock(self, block: Any, keyA: Any=None, keyB: Any=None) -> Tuple[Any, Any]: ...
    def readBlockStr(self, block: Any, keyA: Any=None, keyB: Any=None) -> Any: ...
        #   0: return data
        # ? 0: return data
    def writeBlock(self, block: Any, data: Any, keyA: Any=None, keyB: Any=None) -> Union[Any, Tuple[Any, Any]]: ...
        #   0: return (ERR, code)
        #   0: return Tuple[ERR, code]
        #   1: return stat
        # ? 1: return stat
    def isCardOn(self) -> bool: ...
    def readUid(self) -> Union[Any, str]: ...
        #   0: return ''
        #   0: return str
        #   1: return data_str
        # ? 1: return data_str
    def init(self) -> None: ...
    def _wreg(self, reg: Any, val: Any) -> None: ...
    def _rreg(self, reg: Any) -> Any: ...
        #   0: return self.i2c.readfrom_mem(self.addr,reg,1)[0]
        # ? 0: return self.i2c.readfrom_mem(self.addr, reg, number)[number]
    def _sflags(self, reg: Any, mask: Any) -> None: ...
    def _cflags(self, reg: Any, mask: Any) -> None: ...
    def _tocard(self, cmd: Any, send: Any) -> Tuple[Any, Any, Any]: ...
    def _crc(self, data: Any) -> List[Any, Any]: ...
    def _reset(self) -> None: ...
    def _antenna_on(self, on: Any=bool) -> None: ...
    def _request(self, mode: Any) -> Tuple[Any, Any]: ...
    def _anticoll(self) -> Tuple[Any, Any]: ...
    def _selectTag(self, ser: Any) -> Any: ...
    def _auth(self, mode: Any, addr: Any, sect: Any, ser: Any) -> Any: ...
        #   0: return self._tocard(14,[mode,addr]+sect+ser[:4])[0]
        # ? 0: return self._tocard(number, List[mode, addr]+sect+ser[:number])[number]
    def _stop_crypto1(self) -> None: ...
    def _read(self, addr: Any) -> Optional[Any]: ...
    def _write(self, addr: Any, data: Any) -> Any: ...
        #   0: return stat
        # ? 0: return stat
    def _get_access(self, block: Any, keyA: Any=None, keyB: Any=None) -> Union[Tuple[Any, number], Tuple[None, number]]: ...
    def deinit(self) -> None: ...
