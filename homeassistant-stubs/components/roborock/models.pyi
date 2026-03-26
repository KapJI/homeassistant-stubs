from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from roborock.data import CleanSummaryWithDetail as CleanSummaryWithDetail, Consumable as Consumable, DnDTimer as DnDTimer, HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, NetworkInfo as NetworkInfo
from roborock.devices.device import RoborockDevice as RoborockDevice
from roborock.devices.traits.v1.status import StatusTrait as StatusTrait
from typing import Any
from vacuum_map_parser_base.map_data import MapData as MapData

_LOGGER: Incomplete

def get_device_info(device: RoborockDevice) -> DeviceInfo: ...

@dataclass
class DeviceState:
    status: StatusTrait
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
