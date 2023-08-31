from .const import CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, DOMAIN as DOMAIN
from .coordinator import PurpleAirDataUpdateCoordinator as PurpleAirDataUpdateCoordinator
from _typeshed import Incomplete
from aiopurpleair.models.sensors import SensorModel as SensorModel
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_handle_entry_update(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class PurpleAirEntity(CoordinatorEntity[PurpleAirDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _sensor_index: Incomplete
    _attr_device_info: Incomplete
    _entry: Incomplete
    def __init__(self, coordinator: PurpleAirDataUpdateCoordinator, entry: ConfigEntry, sensor_index: int) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def sensor_data(self) -> SensorModel: ...
