from dataclasses import dataclass
from roborock.containers import HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, NetworkInfo as NetworkInfo
from roborock.roborock_typing import DeviceProp as DeviceProp
from typing import Any

@dataclass
class RoborockHassDeviceInfo:
    device: HomeDataDevice
    network_info: NetworkInfo
    product: HomeDataProduct
    props: DeviceProp
    def as_dict(self) -> dict[str, dict[str, Any]]: ...
    def __init__(self, device, network_info, product, props) -> None: ...

@dataclass
class RoborockA01HassDeviceInfo:
    device: HomeDataDevice
    product: HomeDataProduct
    def as_dict(self) -> dict[str, dict[str, Any]]: ...
    def __init__(self, device, product) -> None: ...

@dataclass
class RoborockMapInfo:
    flag: int
    name: str
    rooms: dict[int, str]
    def __init__(self, flag, name, rooms) -> None: ...
