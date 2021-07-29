import aiohttp
from typing import Any, NamedTuple

WHOAMI_URL: str
WHOAMI_URL_DEV: str
AXIS_A: int
FLATTENING: Any
AXIS_B: float
MILES_PER_KILOMETER: float
MAX_ITERATIONS: int
CONVERGENCE_THRESHOLD: float

class LocationInfo(NamedTuple):
    ip: Any
    country_code: Any
    currency: Any
    region_code: Any
    region_name: Any
    city: Any
    zip_code: Any
    time_zone: Any
    latitude: Any
    longitude: Any
    use_metric: Any

async def async_detect_location_info(session: aiohttp.ClientSession) -> Union[LocationInfo, None]: ...
def distance(lat1: Union[float, None], lon1: Union[float, None], lat2: float, lon2: float) -> Union[float, None]: ...
def vincenty(point1: tuple[float, float], point2: tuple[float, float], miles: bool = ...) -> Union[float, None]: ...
async def _get_whoami(session: aiohttp.ClientSession) -> Union[dict[str, Any], None]: ...
