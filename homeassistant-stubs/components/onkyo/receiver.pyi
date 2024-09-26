import pyeiscp
from dataclasses import dataclass

@dataclass
class Receiver:
    conn: pyeiscp.Connection
    model_name: str
    identifier: str
    name: str
    discovered: bool
    def __init__(self, conn, model_name, identifier, name, discovered) -> None: ...

@dataclass
class ReceiverInfo:
    host: str
    port: int
    model_name: str
    identifier: str
    def __init__(self, host, port, model_name, identifier) -> None: ...
