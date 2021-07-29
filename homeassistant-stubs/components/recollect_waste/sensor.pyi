from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN, LOGGER as LOGGER
from aiorecollect.client import PickupType as PickupType
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME, CONF_NAME as CONF_NAME, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import as_utc as as_utc
from typing import Any

ATTR_PICKUP_TYPES: str
ATTR_AREA_NAME: str
ATTR_NEXT_PICKUP_TYPES: str
ATTR_NEXT_PICKUP_DATE: str
DEFAULT_ATTRIBUTION: str
DEFAULT_NAME: str

def async_get_pickup_type_names(entry: ConfigEntry, pickup_types: list[PickupType]) -> list[str]: ...
async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReCollectWasteSensor(CoordinatorEntity, SensorEntity):
    _attr_device_class: Any
    _attr_extra_state_attributes: Any
    _attr_name: Any
    _attr_unique_id: Any
    _entry: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_state: Any
    def update_from_latest_data(self) -> None: ...
