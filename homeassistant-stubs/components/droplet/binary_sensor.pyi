from .const import DOMAIN as DOMAIN, KEY_HIGH_FLOW as KEY_HIGH_FLOW, KEY_UNUSUAL_FLOW as KEY_UNUSUAL_FLOW
from .coordinator import DropletConfigEntry as DropletConfigEntry, DropletDataCoordinator as DropletDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pydroplet.droplet import Droplet as Droplet
from typing import override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class DropletBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Droplet], bool | None]

BINARY_SENSORS: list[DropletBinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: DropletConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DropletBinarySensor(CoordinatorEntity[DropletDataCoordinator], BinarySensorEntity):
    entity_description: DropletBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DropletDataCoordinator, entity_description: DropletBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
