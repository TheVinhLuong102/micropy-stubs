# make_stub_files: Mon 02 Sep 2019 at 04:45:27

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
    def setString(self, srcString: Any) -> None: ...
    def regenerateString(self) -> Any: ...
        #   0: return json.dumps(self._dictionaryObject)
        # ? 0: return json.dumps(self._dictionaryObject)
    def getAttributeValue(self, srcAttributeKey: Any) -> Any: ...
        #   0: return self._dictionaryObject.get(srcAttributeKey)
        # ? 0: return self._dictionaryObject.get(srcAttributeKey)
    def setAttributeValue(self, srcAttributeKey: Any, srcAttributeValue: Any) -> None: ...
    def validateJSON(self) -> bool: ...
class deviceShadow:
    def __init__(self, srcShadowName: Any, srcIsPersistentSubscribe: Any, srcShadowManager: Any) -> None: ...
    def _doNonPersistentUnsubscribe(self, currentAction: Any) -> None: ...
    def _generalCallback(self, client: Any, userdata: Any, message: Any) -> None: ...
    def _parseTopicAction(self, srcTopic: Any) -> Any: ...
        #   0: return ret
        # ? 0: return ret
    def _parseTopicType(self, srcTopic: Any) -> Any: ...
        #   0: return fragments[5]
        # ? 0: return fragments[number]
    def _parseTopicShadowName(self, srcTopic: Any) -> Any: ...
        #   0: return fragments[2]
        # ? 0: return fragments[number]
    def _timerHandler(self, args: Any) -> None: ...
    def shadowGet(self, srcCallback: Any, srcTimeout: Any) -> Any: ...
        #   0: return currentToken
        # ? 0: return currentToken
    def shadowDelete(self, srcCallback: Any, srcTimeout: Any) -> Any: ...
        #   0: return currentToken
        # ? 0: return currentToken
    def shadowUpdate(self, srcJSONPayload: Any, srcCallback: Any, srcTimeout: Any) -> Any: ...
        #   0: return currentToken
        # ? 0: return currentToken
    def shadowRegisterDeltaCallback(self, srcCallback: Any) -> None: ...
    def shadowUnregisterDeltaCallback(self) -> None: ...
