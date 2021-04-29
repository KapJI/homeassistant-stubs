import json
from typing import Any

class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...

class ExtendedJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any: ...
