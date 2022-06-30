import json
import orjson
from _typeshed import Incomplete
from typing import Any, Final

JSON_ENCODE_EXCEPTIONS: Incomplete
JSON_DECODE_EXCEPTIONS: Incomplete

class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...

def json_encoder_default(obj: Any) -> Any: ...

class ExtendedJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any: ...

def json_bytes(data: Any) -> bytes: ...
def json_dumps(data: Any) -> str: ...
def json_dumps_sorted(data: Any) -> str: ...
json_loads = orjson.loads
JSON_DUMP: Final[Incomplete]
