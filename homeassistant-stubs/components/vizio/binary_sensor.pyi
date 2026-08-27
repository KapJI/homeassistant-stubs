from .coordinator import VizioConfigEntry as VizioConfigEntry, VizioDeviceData as VizioDeviceData
from .entity import VizioDescriptionEntity as VizioDescriptionEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VizioBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[VizioDeviceData], bool | None]

BINARY_SENSORS: tuple[VizioBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: VizioConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VizioBinarySensor(VizioDescriptionEntity, BinarySensorEntity):
    entity_description: VizioBinarySensorEntityDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
