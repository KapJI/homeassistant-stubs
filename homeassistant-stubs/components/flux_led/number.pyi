from . import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .const import DOMAIN as DOMAIN, EFFECT_SPEED_SUPPORT_MODES as EFFECT_SPEED_SUPPORT_MODES
from .entity import FluxEntity as FluxEntity
from .util import _effect_brightness as _effect_brightness, _hass_color_modes as _hass_color_modes
from homeassistant import config_entries as config_entries
from homeassistant.components.number import NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxNumber(FluxEntity, CoordinatorEntity, NumberEntity):
    _attr_min_value: int
    _attr_max_value: int
    _attr_step: int
    _attr_mode: Any
    _attr_icon: str
    _attr_name: Any
    def __init__(self, coordinator: FluxLedUpdateCoordinator, unique_id: Union[str, None], name: str) -> None: ...
    @property
    def value(self) -> float: ...
    async def async_set_value(self, value: float) -> None: ...
