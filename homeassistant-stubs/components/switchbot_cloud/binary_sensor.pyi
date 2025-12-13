from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, SwitchBotAPI as SwitchBotAPI
from typing import Any

@dataclass(frozen=True)
class SwitchBotCloudBinarySensorEntityDescription(BinarySensorEntityDescription):
    on_value: bool | str = ...
    value_fn: Callable[[dict[str, Any]], bool | None] | None = ...

CALIBRATION_DESCRIPTION: Incomplete
DOOR_OPEN_DESCRIPTION: Incomplete
MOVE_DETECTED_DESCRIPTION: Incomplete
IS_LIGHT_DESCRIPTION: Incomplete
LEAK_DESCRIPTION: Incomplete
OPEN_DESCRIPTION: Incomplete
BINARY_SENSOR_DESCRIPTIONS_BY_DEVICE_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudBinarySensor(SwitchBotCloudEntity, BinarySensorEntity):
    entity_description: SwitchBotCloudBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device, coordinator: SwitchBotCoordinator, description: SwitchBotCloudBinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    def _set_attributes(self) -> None: ...
