from . import SwitchBotCoordinator as SwitchBotCoordinator, SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudLock(SwitchBotCloudEntity, LockEntity):
    _attr_name: Incomplete
    __model: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> None: ...
    _attr_is_locked: Incomplete
    _attr_supported_features: Incomplete
    def _set_attributes(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
