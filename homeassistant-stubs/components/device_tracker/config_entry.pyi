from .const import ATTR_HOST_NAME as ATTR_HOST_NAME, ATTR_IP as ATTR_IP, ATTR_MAC as ATTR_MAC, ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components import zone as zone
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import StateType as StateType

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BaseTrackerEntity(Entity):
    @property
    def battery_level(self) -> Union[int, None]: ...
    @property
    def source_type(self) -> str: ...
    @property
    def state_attributes(self) -> dict[str, StateType]: ...

class TrackerEntity(BaseTrackerEntity):
    @property
    def should_poll(self) -> bool: ...
    @property
    def force_update(self) -> bool: ...
    @property
    def location_accuracy(self) -> int: ...
    @property
    def location_name(self) -> Union[str, None]: ...
    @property
    def latitude(self) -> Union[float, None]: ...
    @property
    def longitude(self) -> Union[float, None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def state_attributes(self) -> dict[str, StateType]: ...

class ScannerEntity(BaseTrackerEntity):
    @property
    def ip_address(self) -> Union[str, None]: ...
    @property
    def mac_address(self) -> Union[str, None]: ...
    @property
    def hostname(self) -> Union[str, None]: ...
    @property
    def state(self) -> str: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def state_attributes(self) -> dict[str, StateType]: ...