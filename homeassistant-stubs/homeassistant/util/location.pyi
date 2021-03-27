import aiohttp
from collections import namedtuple
from typing import Any, Optional, Tuple

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

async def async_detect_location_info(session: aiohttp.ClientSession) -> Optional[LocationInfo]: ...
def distance(lat1: Optional[float], lon1: Optional[float], lat2: float, lon2: float) -> Optional[float]: ...
def vincenty(point1: Tuple[float, float], point2: Tuple[float, float], miles: bool=...) -> Optional[float]: ...
