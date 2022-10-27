from .const import ATTR_THEME as ATTR_THEME, DOMAIN as DOMAIN, INFRARED_BRIGHTNESS as INFRARED_BRIGHTNESS, INFRARED_BRIGHTNESS_VALUES_MAP as INFRARED_BRIGHTNESS_VALUES_MAP
from .coordinator import LIFXSensorUpdateCoordinator as LIFXSensorUpdateCoordinator, LIFXUpdateCoordinator as LIFXUpdateCoordinator
from .entity import LIFXSensorEntity as LIFXSensorEntity
from .util import lifx_features as lifx_features
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

THEME_NAMES: Incomplete
INFRARED_BRIGHTNESS_ENTITY: Incomplete
THEME_ENTITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LIFXInfraredBrightnessSelectEntity(LIFXSensorEntity, SelectEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, coordinator: LIFXSensorUpdateCoordinator, description: SelectEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class LIFXThemeSelectEntity(LIFXSensorEntity, SelectEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, coordinator: LIFXSensorUpdateCoordinator, description: SelectEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
