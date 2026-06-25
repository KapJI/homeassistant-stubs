from .const import ATTRIBUTION as ATTRIBUTION, CONF_FILTER as CONF_FILTER, CONF_REAL_TIME as CONF_REAL_TIME, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .hub import GTIHub as GTIHub, HVVConfigEntry as HVVConfigEntry
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import ATTR_ID as ATTR_ID, CONF_OFFSET as CONF_OFFSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import Throttle as Throttle
from homeassistant.util.dt import get_time_zone as get_time_zone, utcnow as utcnow
from typing import Any

MIN_TIME_BETWEEN_UPDATES: Incomplete
MAX_LIST: int
MAX_TIME_OFFSET: int
ATTR_DEPARTURE: str
ATTR_LINE: str
ATTR_ORIGIN: str
ATTR_DIRECTION: str
ATTR_TYPE: str
ATTR_DELAY: str
ATTR_NEXT: str
ATTR_CANCELLED: str
ATTR_EXTRA: str
PARALLEL_UPDATES: int
BERLIN_TIME_ZONE: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HVVConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HVVDepartureSensor(SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_has_entity_name: bool
    _attr_available: bool
    config_entry: Incomplete
    station_name: Incomplete
    _last_error: type[Exception] | Exception | None
    _attr_extra_state_attributes: Incomplete
    gti: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HVVConfigEntry, session: ClientSession, hub: GTIHub) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self, **kwargs: Any) -> None: ...
