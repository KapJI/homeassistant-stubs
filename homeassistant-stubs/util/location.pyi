import aiohttp
from collections import namedtuple
from typing import Any

ELEVATION_URL: str
IP_API: str
IPAPI: str
AXIS_A: int
FLATTENING: Any
AXIS_B: float
MILES_PER_KILOMETER: float
MAX_ITERATIONS: int
CONVERGENCE_THRESHOLD: float

LocationInfo = namedtuple('LocationInfo', ['ip', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'zip_code', 'time_zone', 'latitude', 'longitude', 'use_metric'])

async def async_detect_location_info(session: aiohttp.ClientSession) -> Union[LocationInfo, None]: ...
def distance(lat1: Union[float, None], lon1: Union[float, None], lat2: float, lon2: float) -> Union[float, None]: ...
def vincenty(point1: tuple[float, float], point2: tuple[float, float], miles: bool=...) -> Union[float, None]: ...
async def _get_ipapi(session: aiohttp.ClientSession) -> Union[dict[str, Any], None]: ...
async def _get_ip_api(session: aiohttp.ClientSession) -> Union[dict[str, Any], None]: ...
