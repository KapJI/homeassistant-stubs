from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import CharacteristicEntity as CharacteristicEntity
from _typeshed import Incomplete
from aiohomekit.model.characteristics import Characteristic as Characteristic
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_ECOBEE_MODE_TO_TEXT: Incomplete
_ECOBEE_MODE_TO_NUMBERS: Incomplete

class EcobeeModeSelect(CharacteristicEntity, SelectEntity):
    _attr_options: Incomplete
    _attr_translation_key: str
    @property
    def name(self) -> str: ...
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
