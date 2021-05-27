from typing import Dict, TypedDict

KrakenResponse = Dict[str, Dict[str, float]]

class SensorType(TypedDict):
    name: str
    enabled_by_default: bool

DEFAULT_SCAN_INTERVAL: int
DEFAULT_TRACKED_ASSET_PAIR: str
DISPATCH_CONFIG_UPDATED: str
CONF_TRACKED_ASSET_PAIRS: str
DOMAIN: str
SENSOR_TYPES: list[SensorType]
