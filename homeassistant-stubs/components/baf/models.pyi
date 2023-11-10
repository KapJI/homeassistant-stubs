import asyncio
from aiobafi6 import Device as Device
from dataclasses import dataclass

@dataclass
class BAFData:
    device: Device
    run_future: asyncio.Future
    def __init__(self, device, run_future) -> None: ...

@dataclass
class BAFDiscovery:
    ip_address: str
    name: str
    uuid: str
    model: str
    def __init__(self, ip_address, name, uuid, model) -> None: ...
