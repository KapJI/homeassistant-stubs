from .const import DEFAULT_RETRY_COUNT as DEFAULT_RETRY_COUNT, DEFAULT_RETRY_TIMEOUT as DEFAULT_RETRY_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tololib.message_info import SettingsInfo as SettingsInfo, StatusInfo as StatusInfo
from typing import NamedTuple

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ToloSaunaData(NamedTuple):
    status: StatusInfo
    settings: SettingsInfo

class ToloSaunaUpdateCoordinator(DataUpdateCoordinator[ToloSaunaData]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> ToloSaunaData: ...
    def _get_tolo_sauna_data(self) -> ToloSaunaData: ...

class ToloSaunaCoordinatorEntity(CoordinatorEntity[ToloSaunaUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
