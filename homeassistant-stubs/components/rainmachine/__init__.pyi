from .config_flow import get_client_controller as get_client_controller
from .const import CONF_ZONE_RUN_TIME as CONF_ZONE_RUN_TIME, DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROGRAMS as DATA_PROGRAMS, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DATA_ZONES as DATA_ZONES, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.network import is_ip_address as is_ip_address
from regenmaschine.controller import Controller
from typing import Any

DEFAULT_ATTRIBUTION: str
DEFAULT_ICON: str
DEFAULT_SSL: bool
DEFAULT_UPDATE_INTERVAL: Any
CONFIG_SCHEMA: Any
PLATFORMS: Any
UPDATE_INTERVALS: Any
CONF_CONDITION: str
CONF_DEWPOINT: str
CONF_ET: str
CONF_MAXRH: str
CONF_MAXTEMP: str
CONF_MINRH: str
CONF_MINTEMP: str
CONF_PRESSURE: str
CONF_QPF: str
CONF_RAIN: str
CONF_SECONDS: str
CONF_SOLARRAD: str
CONF_TEMPERATURE: str
CONF_TIMESTAMP: str
CONF_WEATHER: str
CONF_WIND: str
CV_WX_DATA_VALID_PERCENTAGE: Any
CV_WX_DATA_VALID_TEMP_RANGE: Any
CV_WX_DATA_VALID_RAIN_RANGE: Any
CV_WX_DATA_VALID_WIND_SPEED: Any
CV_WX_DATA_VALID_PRESSURE: Any
CV_WX_DATA_VALID_SOLARRAD: Any
SERVICE_NAME_PAUSE_WATERING: str
SERVICE_NAME_PUSH_WEATHER_DATA: str
SERVICE_NAME_STOP_ALL: str
SERVICE_NAME_UNPAUSE_WATERING: str
SERVICE_SCHEMA: Any
SERVICE_PAUSE_WATERING_SCHEMA: Any
SERVICE_PUSH_WEATHER_DATA_SCHEMA: Any

def async_get_controller_for_service_call(hass: HomeAssistant, call: ServiceCall) -> Controller: ...
async def async_update_programs_and_zones(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class RainMachineEntity(CoordinatorEntity):
    _attr_device_info: Any
    _attr_extra_state_attributes: Any
    _attr_name: Any
    _attr_unique_id: Any
    _controller: Any
    entity_description: Any
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, controller: Controller, description: EntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
