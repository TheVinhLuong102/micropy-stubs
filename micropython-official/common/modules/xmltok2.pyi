# make_stub_files: Wed 19 Jun 2019 at 15:04:41

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class XMLSyntaxError(Exception): ...
class XMLTokenizer:
    def __init__(self, f: Any) -> None: ...
    def curch(self) -> Any: ...
        #   0: return self.c
        # ? 0: return self.c
    def getch(self) -> Any: ...
        #   0: return c
        # ? 0: return c
    def eof(self) -> bool: ...
    def nextch(self) -> Any: ...
        #   0: return self.c
        # ? 0: return self.c
    def skip_ws(self) -> None: ...
    def isident(self) -> Any: ...
        #   0: return self.curch().isalpha()
        # ? 0: return self.curch().isalpha()
    def getident(self) -> Any: ...
        #   0: return ident
        # ? 0: return ident
    def putnsident(self, res: Any) -> None: ...
    def match(self, c: Any) -> bool: ...
    def expect(self, c: Any) -> None: ...
    def lex_attrs_till(self, res: Any) -> None: ...
    def tokenize(self) -> None: ...
def gfind(gen: Any, pred: Any) -> int: ...
def text_of(gen: Any, tag: Any) -> Union[Any, bool]:
    #   0: return bool
    #   0: return bool
    #   1: return t[1]==tag[0] and t[2]==tag[1]
    #   1: return bool
    #   2: return t[2]==tag
    #   2: return bool
    #   3: return res[1]
    # ? 3: return res[number]
    def match_tag(t: Any) -> bool: ...
def tokenize(file: Any) -> Any: ...
    #   0: return XMLTokenizer(file).tokenize()
    # ? 0: return XMLTokenizer(file).tokenize()
