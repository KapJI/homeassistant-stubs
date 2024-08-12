from dataclasses import dataclass
from uuid import UUID

@dataclass
class NetatmoArea:
    area_name: str
    lat_ne: float
    lon_ne: float
    lat_sw: float
    lon_sw: float
    mode: str
    show_on_map: bool
    uuid: UUID = ...
    def __init__(self, area_name, lat_ne, lon_ne, lat_sw, lon_sw, mode, show_on_map, uuid=...) -> None: ...
