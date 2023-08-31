from . import Trackables as Trackables, TractiveClient as TractiveClient
from .const import CLIENT as CLIENT, DOMAIN as DOMAIN, TRACKABLES as TRACKABLES, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class TractiveBinarySensor(TractiveEntity, BinarySensorEntity):
    _attr_unique_id: Incomplete
    _attr_available: bool
    entity_description: Incomplete
    def __init__(self, client: TractiveClient, item: Trackables, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    def handle_status_update(self, event: dict[str, Any]) -> None: ...

SENSOR_TYPE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
