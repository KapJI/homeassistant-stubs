from .const import CONF_PLACE_ID as CONF_PLACE_ID, CONF_SERVICE_ID as CONF_SERVICE_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiorecollect.client import PickupType as PickupType
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FRIENDLY_NAME as CONF_FRIENDLY_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

ATTR_PICKUP_TYPES: str
ATTR_AREA_NAME: str
SENSOR_TYPE_CURRENT_PICKUP: str
SENSOR_TYPE_NEXT_PICKUP: str
SENSOR_DESCRIPTIONS: Incomplete

def async_get_pickup_type_names(entry: ConfigEntry, pickup_types: list[PickupType]) -> list[str]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReCollectWasteSensor(CoordinatorEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...
