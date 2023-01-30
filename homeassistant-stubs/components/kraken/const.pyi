from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import TypedDict

class KrakenResponseEntry(TypedDict):
    ask: tuple[float, float, float]
    bid: tuple[float, float, float]
    last_trade_closed: tuple[float, float]
    volume: tuple[float, float]
    volume_weighted_average: tuple[float, float]
    number_of_trades: tuple[int, int]
    low: tuple[float, float]
    high: tuple[float, float]
    opening_price: float
KrakenResponse = dict[str, KrakenResponseEntry]
DEFAULT_SCAN_INTERVAL: int
DEFAULT_TRACKED_ASSET_PAIR: str
DISPATCH_CONFIG_UPDATED: str
CONF_TRACKED_ASSET_PAIRS: str
DOMAIN: str

class KrakenRequiredKeysMixin:
    value_fn: Callable[[DataUpdateCoordinator[KrakenResponse], str], Union[float, int]]
    def __init__(self, value_fn) -> None: ...

class KrakenSensorEntityDescription(SensorEntityDescription, KrakenRequiredKeysMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[KrakenSensorEntityDescription, ...]
