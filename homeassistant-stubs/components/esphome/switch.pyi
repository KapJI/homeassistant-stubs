from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, SwitchInfo, SwitchState
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeSwitch(EsphomeEntity[SwitchInfo, SwitchState], SwitchEntity):
    _attr_assumed_state: Incomplete
    _attr_device_class: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
