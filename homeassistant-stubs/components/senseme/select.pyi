from .const import DOMAIN as DOMAIN
from .entity import SensemeEntity as SensemeEntity
from aiosenseme import SensemeFan as SensemeFan
from aiosenseme.device import SensemeDevice as SensemeDevice
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SMART_MODE_TO_HASS: Any
HASS_TO_SMART_MODE: Any

class SenseMESelectEntityDescriptionMixin:
    value_fn: Callable[[SensemeFan], str]
    set_fn: Callable[[SensemeFan, str], None]
    def __init__(self, value_fn, set_fn) -> None: ...

class SenseMESelectEntityDescription(SelectEntityDescription, SenseMESelectEntityDescriptionMixin):
    def __init__(self, value_fn, set_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

def _set_smart_mode(device: SensemeDevice, value: str) -> None: ...

FAN_SELECTS: Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HASensemeSelect(SensemeEntity, SelectEntity):
    entity_description: SenseMESelectEntityDescription
    _attr_options: Any
    _attr_unique_id: Any
    def __init__(self, device: SensemeFan, description: SenseMESelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
