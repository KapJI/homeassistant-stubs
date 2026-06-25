from dataclasses import dataclass, field
from pyatmo.modules.device_types import DeviceType as NetatmoDeviceType
from uuid import UUID, uuid4

def device_type_to_str(device_type: NetatmoDeviceType) -> str: ...

@dataclass
class NetatmoArea:
    area_name: str
    lat_ne: float
    lon_ne: float
    lat_sw: float
    lon_sw: float
    mode: str
    show_on_map: bool
    uuid: UUID = field(default_factory=uuid4)
