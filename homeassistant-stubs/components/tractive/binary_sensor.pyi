from . import Trackables as Trackables, TractiveClient as TractiveClient, TractiveConfigEntry as TractiveConfigEntry
from .const import ATTR_POWER_SAVING as ATTR_POWER_SAVING, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

class TractiveBinarySensor(TractiveEntity, BinarySensorEntity):
    _attr_unique_id: Incomplete
    _attr_available: bool
    entity_description: Incomplete
    def __init__(self, client: TractiveClient, item: Trackables, description: TractiveBinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    @callback
    def handle_status_update(self, event: dict[str, Any]) -> None: ...

@dataclass(frozen=True, kw_only=True)
class TractiveBinarySensorEntityDescription(BinarySensorEntityDescription):
    supported: Callable[[dict], bool] = ...

SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TractiveConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
