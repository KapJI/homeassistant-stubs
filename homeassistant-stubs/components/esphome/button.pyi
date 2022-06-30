from . import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import ButtonInfo, EntityState
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeButton(EsphomeEntity[ButtonInfo, EntityState], ButtonEntity):
    @property
    def device_class(self) -> Union[ButtonDeviceClass, None]: ...
    def _on_device_update(self) -> None: ...
    async def async_press(self) -> None: ...
