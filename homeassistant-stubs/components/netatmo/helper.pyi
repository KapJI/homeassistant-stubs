import pyatmo
from uuid import UUID

class NetatmoArea:
    area_name: str
    lat_ne: float
    lon_ne: float
    lat_sw: float
    lon_sw: float
    mode: str
    show_on_map: bool
    uuid: UUID

def get_all_home_ids(home_data: Union[pyatmo.HomeData, None]) -> list[str]: ...
def update_climate_schedules(home_ids: list[str], schedules: dict) -> dict: ...
