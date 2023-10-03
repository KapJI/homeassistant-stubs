from elkm1_lib import Elk as Elk
from typing import Any

class ELKM1Data:
    elk: Elk
    prefix: str
    mac: str | None
    auto_configure: bool
    config: dict[str, Any]
    keypads: dict[str, Any]
    def __init__(self, elk, prefix, mac, auto_configure, config, keypads) -> None: ...
