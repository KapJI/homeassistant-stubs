import aiohttp
from _typeshed import Incomplete
from typing import Any, NamedTuple

WHOAMI_URL: str
WHOAMI_URL_DEV: str
AXIS_A: int
FLATTENING: Incomplete
AXIS_B: float
MILES_PER_KILOMETER: float
MAX_ITERATIONS: int
CONVERGENCE_THRESHOLD: float

class LocationInfo(NamedTuple):
    ip: Incomplete
    country_code: Incomplete
    currency: Incomplete
    region_code: Incomplete
    region_name: Incomplete
    city: Incomplete
    zip_code: Incomplete
    time_zone: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    use_metric: Incomplete

async def async_detect_location_info(session: aiohttp.ClientSession) -> Union[LocationInfo, None]: ...
def distance(lat1: Union[float, None], lon1: Union[float, None], lat2: float, lon2: float) -> Union[float, None]: ...
def vincenty(point1: tuple[float, float], point2: tuple[float, float], miles: bool = ...) -> Union[float, None]: ...
async def _get_whoami(session: aiohttp.ClientSession) -> Union[dict[str, Any], None]: ...
