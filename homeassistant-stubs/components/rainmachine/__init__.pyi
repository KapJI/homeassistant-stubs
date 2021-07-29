from .config_flow import get_client_controller as get_client_controller
from .const import CONF_ZONE_RUN_TIME as CONF_ZONE_RUN_TIME, DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.network import is_ip_address as is_ip_address
from regenmaschine.controller import Controller as Controller
from typing import Any

DEFAULT_ATTRIBUTION: str
DEFAULT_ICON: str
DEFAULT_SSL: bool
DEFAULT_UPDATE_INTERVAL: Any
CONFIG_SCHEMA: Any
PLATFORMS: Any

async def async_update_programs_and_zones(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class RainMachineEntity(CoordinatorEntity):
    _attr_device_info: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    _controller: Any
    _entity_type: Any
    def __init__(self, coordinator: DataUpdateCoordinator, controller: Controller, entity_type: str) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
