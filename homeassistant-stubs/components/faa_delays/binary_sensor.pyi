from . import FAAConfigEntry as FAAConfigEntry, FAADataUpdateCoordinator as FAADataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from faadelays import Airport as Airport
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class FaaDelaysBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Airport], bool | None]
    extra_state_attributes_fn: Callable[[Airport], Mapping[str, Any]]

FAA_BINARY_SENSORS: tuple[FaaDelaysBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FAAConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FAABinarySensor(CoordinatorEntity[FAADataUpdateCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: FaaDelaysBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FAADataUpdateCoordinator, entry_id: str, description: FaaDelaysBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
