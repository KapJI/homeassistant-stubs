from . import LutronConfigEntry as LutronConfigEntry
from .entity import LutronDevice as LutronDevice
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylutron import OccupancyGroup
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LutronOccupancySensor(LutronDevice, BinarySensorEntity):
    _lutron_device: OccupancyGroup
    _attr_device_class: Incomplete
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    _attr_is_on: Incomplete
    def _update_attrs(self) -> None: ...
