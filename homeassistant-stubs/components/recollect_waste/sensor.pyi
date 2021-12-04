from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DOMAIN as DOMAIN
from aiorecollect.client import PickupType as PickupType
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME, DEVICE_CLASS_DATE as DEVICE_CLASS_DATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_PICKUP_TYPES: str
ATTR_AREA_NAME: str
ATTR_NEXT_PICKUP_TYPES: str
ATTR_NEXT_PICKUP_DATE: str
DEFAULT_NAME: str
PLATFORM_SCHEMA: Any

def async_get_pickup_type_names(entry: ConfigEntry, pickup_types: list[PickupType]) -> list[str]: ...
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
    _attr_native_value: Any
    def update_from_latest_data(self) -> None: ...
