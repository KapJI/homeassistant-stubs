from dataclasses import dataclass

@dataclass
class BAFDiscovery:
    ip_address: str
    name: str
    uuid: str
    model: str
    def __init__(self, ip_address, name, uuid, model) -> None: ...
