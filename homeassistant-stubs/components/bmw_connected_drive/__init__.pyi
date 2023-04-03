from .const import ATTRIBUTION as ATTRIBUTION, ATTR_VIN as ATTR_VIN, CONF_READ_ONLY as CONF_READ_ONLY, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_SCHEMA: Incomplete
DEFAULT_OPTIONS: Incomplete
PLATFORMS: Incomplete
SERVICE_UPDATE_STATE: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _async_migrate_options_from_data_if_missing(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def _async_migrate_entries(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class BMWBaseEntity(CoordinatorEntity[BMWDataUpdateCoordinator]):
    coordinator: BMWDataUpdateCoordinator
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    vehicle: Incomplete
    _attrs: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle) -> None: ...
    async def async_added_to_hass(self) -> None: ...
