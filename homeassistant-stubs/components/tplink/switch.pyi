from . import legacy_device_id as legacy_device_id
from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity, async_refresh_after as async_refresh_after
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import SmartDevice as SmartDevice, SmartPlug
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmartPlugLedSwitch(CoordinatedTPLinkEntity, SwitchEntity):
    coordinator: TPLinkDataUpdateCoordinator
    device: SmartPlug
    _attr_entity_category: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, device: SmartPlug, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    @property
    def icon(self) -> str: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...

class SmartPlugSwitch(CoordinatedTPLinkEntity, SwitchEntity):
    coordinator: TPLinkDataUpdateCoordinator
    _attr_unique_id: Any
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
