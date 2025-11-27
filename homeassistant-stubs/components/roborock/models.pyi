from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from roborock.data import CleanSummaryWithDetail as CleanSummaryWithDetail, Consumable as Consumable, DnDTimer as DnDTimer, HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, NetworkInfo as NetworkInfo, Status as Status
from typing import Any
from vacuum_map_parser_base.map_data import MapData as MapData

_LOGGER: Incomplete

@dataclass
class DeviceState:
    status: Status
    dnd_timer: DnDTimer
    consumable: Consumable
    clean_summary: CleanSummaryWithDetail

@dataclass
class RoborockHassDeviceInfo:
    device: HomeDataDevice
    network_info: NetworkInfo
    product: HomeDataProduct
    def as_dict(self) -> dict[str, dict[str, Any]]: ...

@dataclass
class RoborockA01HassDeviceInfo:
    device: HomeDataDevice
    product: HomeDataProduct
    def as_dict(self) -> dict[str, dict[str, Any]]: ...

@dataclass
class RoborockMapInfo:
    flag: int
    name: str
    image: bytes | None
    last_updated: datetime
    map_data: MapData | None
