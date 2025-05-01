from .const import DOMAIN as DOMAIN
from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge
from .entity import ComelitBridgeBaseEntity as ComelitBridgeBaseEntity
from _typeshed import Incomplete
from aiocomelit import ComelitSerialBridgeObject as ComelitSerialBridgeObject
from enum import StrEnum
from homeassistant.components.humidifier import HumidifierAction as HumidifierAction, HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityFeature as HumidifierEntityFeature, MODE_AUTO as MODE_AUTO, MODE_NORMAL as MODE_NORMAL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

class HumidifierComelitMode(StrEnum):
    AUTO = 'A'
    OFF = 'O'
    LOWER = 'L'
    UPPER = 'U'

class HumidifierComelitCommand(StrEnum):
    OFF = 'off'
    ON = 'on'
    MANUAL = 'man'
    SET = 'set'
    AUTO = 'auto'
    LOWER = 'lower'
    UPPER = 'upper'

MODE_TO_ACTION: dict[str, HumidifierComelitCommand]

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitHumidifierEntity(ComelitBridgeBaseEntity, HumidifierEntity):
    _attr_supported_features: Incomplete
    _attr_available_modes: Incomplete
    _attr_min_humidity: int
    _attr_max_humidity: int
    _attr_unique_id: Incomplete
    _attr_device_class: Incomplete
    _attr_translation_key: Incomplete
    _active_mode: Incomplete
    _active_action: Incomplete
    _set_command: Incomplete
    def __init__(self, coordinator: ComelitSerialBridge, device: ComelitSerialBridgeObject, config_entry_entry_id: str, active_mode: HumidifierComelitMode, active_action: HumidifierAction, set_command: HumidifierComelitCommand, device_class: HumidifierDeviceClass) -> None: ...
    _attr_action: Incomplete
    _attr_current_humidity: Incomplete
    _attr_is_on: Incomplete
    _attr_mode: Incomplete
    _attr_target_humidity: Incomplete
    def _update_attributes(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
