from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudSwitch(SwitchBotCloudEntity, SwitchEntity):
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _set_attributes(self) -> None: ...

class SwitchBotCloudRemoteSwitch(SwitchBotCloudSwitch):
    def _set_attributes(self) -> None: ...

class SwitchBotCloudPlugSwitch(SwitchBotCloudSwitch):
    _attr_device_class: Incomplete

class SwitchBotCloudRelaySwitchSwitch(SwitchBotCloudSwitch):
    _attr_is_on: Incomplete
    def _set_attributes(self) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator) -> SwitchBotCloudSwitch: ...
