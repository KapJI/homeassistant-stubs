import asyncio
from .const import API_SENSOR_PAIRED_SENSOR_STATUS as API_SENSOR_PAIRED_SENSOR_STATUS, API_SENSOR_PAIR_DUMP as API_SENSOR_PAIR_DUMP, API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_VALVE_STATUS as API_VALVE_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, CONF_UID as CONF_UID, DATA_CLIENT as DATA_CLIENT, DATA_COORDINATOR as DATA_COORDINATOR, DATA_COORDINATOR_PAIRED_SENSOR as DATA_COORDINATOR_PAIRED_SENSOR, DATA_PAIRED_SENSOR_MANAGER as DATA_PAIRED_SENSOR_MANAGER, DATA_UNSUB_DISPATCHER_CONNECT as DATA_UNSUB_DISPATCHER_CONNECT, DOMAIN as DOMAIN, LOGGER as LOGGER, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from .util import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from aioguardian import Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class PairedSensorManager:
    _api_lock: Any
    _client: Any
    _entry: Any
    _hass: Any
    _paired_uids: Any
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, client: Client, api_lock: asyncio.Lock) -> None: ...
    async def async_pair_sensor(self, uid: str) -> None: ...
    async def async_process_latest_paired_sensor_uids(self) -> None: ...
    async def async_unpair_sensor(self, uid: str) -> None: ...

class GuardianEntity(CoordinatorEntity):
    _attr_device_class: Any
    _attr_device_info: Any
    _attr_extra_state_attributes: Any
    _attr_icon: Any
    _attr_name: Any
    _entry: Any
    def __init__(self, entry: ConfigEntry, kind: str, name: str, device_class: Union[str, None], icon: Union[str, None]) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...

class PairedSensorEntity(GuardianEntity):
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    _kind: Any
    coordinator: Any
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, kind: str, name: str, device_class: Union[str, None], icon: Union[str, None]) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class ValveControllerEntity(GuardianEntity):
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    _kind: Any
    coordinators: Any
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, DataUpdateCoordinator], kind: str, name: str, device_class: Union[str, None], icon: Union[str, None]) -> None: ...
    @property
    def available(self) -> bool: ...
    async def _async_continue_entity_setup(self) -> None: ...
    def async_add_coordinator_update_listener(self, api: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
