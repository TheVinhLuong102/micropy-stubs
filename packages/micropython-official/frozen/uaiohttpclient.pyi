# make_stub_files: Wed 17 Jul 2019 at 02:46:15

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class ClientResponse:
    def __init__(self, reader: Any) -> None: ...
    def read(self, sz: Any=-1) -> Any: ...
        #   0: return yield from self.content.read(sz)
        # ? 0: return yield from self.content.read(sz)
    def aclose(self) -> None: ...
    def __repr__(self) -> str: ...
class ChunkedClientResponse(ClientResponse):
    def __init__(self, reader: Any) -> None: ...
    def read(self, sz: Any=4*1024*1024) -> Union[Any, bytes]: ...
        #   0: return b''
        #   0: return bytes
        #   1: return data
        # ? 1: return data
    def __repr__(self) -> str: ...
def request_raw(method: Any, url: Any) -> Any: ...
    #   0: return reader
    # ? 0: return reader
def request(method: Any, url: Any) -> Any: ...
    #   0: return resp
    # ? 0: return resp
