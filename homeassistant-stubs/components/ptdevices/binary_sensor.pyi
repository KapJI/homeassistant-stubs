from .coordinator import PTDevicesConfigEntry as PTDevicesConfigEntry, PTDevicesCoordinator as PTDevicesCoordinator
from .entity import PTDevicesEntity as PTDevicesEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override

PARALLEL_UPDATES: int

class PTDevicesBinarySensors(StrEnum):
    DEVICE_BATTERY_STATUS = 'battery_status'
    DEVICE_EXTERNAL_POWER = 'external_power'

@dataclass(kw_only=True, frozen=True)
class PTDevicesBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[dict[str, StateType]], bool | None]

BINARY_SENSOR_DESCRIPTIONS: tuple[PTDevicesBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PTDevicesConfigEntry, async_add_entity: AddConfigEntryEntitiesCallback) -> None: ...

class PTDevicesBinarySensorEntity(PTDevicesEntity, BinarySensorEntity):
    entity_description: PTDevicesBinarySensorEntityDescription
    def __init__(self, coordinator: PTDevicesCoordinator, description: PTDevicesBinarySensorEntityDescription, device_id: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
