from .coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any

_LOGGER: Incomplete

class BaseBetaFirmwareSwitch(SwitchEntity, RestoreEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_translation_key: str
    _coordinator: Incomplete
    _config_entry: Incomplete
    def __init__(self, coordinator: FirmwareUpdateCoordinator, config_entry: ConfigEntry) -> None: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _update_coordinator_prerelease(self) -> None: ...
