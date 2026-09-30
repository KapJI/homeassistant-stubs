from .const import ATTR_THEME as ATTR_THEME, INFRARED_BRIGHTNESS as INFRARED_BRIGHTNESS, INFRARED_LEVELS as INFRARED_LEVELS
from .coordinator import LIFXConfigEntry as LIFXConfigEntry, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXEntity as LIFXEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
THEME_NAMES: Incomplete
INFRARED_BRIGHTNESS_ENTITY: Incomplete
THEME_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LIFXConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LIFXInfraredBrightnessSelectEntity(LIFXEntity, SelectEntity):
    _attr_current_option: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: SelectEntityDescription) -> None: ...
    @callback
    @override
    def _async_update_attrs(self) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...

class LIFXThemeSelectEntity(LIFXEntity, SelectEntity):
    _attr_current_option: Incomplete
    def __init__(self, coordinator: LIFXUpdateCoordinator, description: SelectEntityDescription) -> None: ...
    @callback
    @override
    def _async_update_attrs(self) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
