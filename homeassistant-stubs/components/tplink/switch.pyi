from . import legacy_device_id as legacy_device_id
from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity, async_refresh_after as async_refresh_after
from .models import TPLinkData as TPLinkData
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import SmartDevice as SmartDevice, SmartPlug
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmartPlugLedSwitch(CoordinatedTPLinkEntity, SwitchEntity):
    device: SmartPlug
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: SmartPlug, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    _attr_icon: Incomplete
    def _async_update_attrs(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...

class SmartPlugSwitch(CoordinatedTPLinkEntity, SwitchEntity):
    _attr_name: str | None
    _attr_unique_id: Incomplete
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...

class SmartPlugSwitchChild(SmartPlugSwitch):
    _plug: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator, plug: SmartDevice) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
