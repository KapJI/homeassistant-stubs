from .entity import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import ButtonInfo, EntityInfo as EntityInfo, EntityState
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeButton(EsphomeEntity[ButtonInfo, EntityState], ButtonEntity):
    _attr_device_class: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    def _on_device_update(self) -> None: ...
    async def async_press(self) -> None: ...
