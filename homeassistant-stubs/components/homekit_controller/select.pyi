from . import CharacteristicEntity as CharacteristicEntity, KNOWN_DEVICES as KNOWN_DEVICES
from .const import DEVICE_CLASS_ECOBEE_MODE as DEVICE_CLASS_ECOBEE_MODE
from aiohomekit.model.characteristics import Characteristic as Characteristic
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_ECOBEE_MODE_TO_TEXT: Any
_ECOBEE_MODE_TO_NUMBERS: Any

class EcobeeModeSelect(CharacteristicEntity, SelectEntity):
    _attr_options: Any
    _attr_device_class: Any
    @property
    def name(self) -> str: ...
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
