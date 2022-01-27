from . import Trackables as Trackables
from .const import CLIENT as CLIENT, DOMAIN as DOMAIN, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, TRACKABLES as TRACKABLES, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

TRACKERS_WITH_BUILTIN_BATTERY: Any

class TractiveBinarySensor(TractiveEntity, BinarySensorEntity):
    _attr_name: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, user_id: str, item: Trackables, description: BinarySensorEntityDescription) -> None: ...
    _attr_available: bool
    def handle_server_unavailable(self) -> None: ...
    _attr_is_on: Any
    def handle_hardware_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...

SENSOR_TYPE: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
