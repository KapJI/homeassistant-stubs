from . import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator
from .const import CONF_MAX_AVAILABLE_POWER_KEY as CONF_MAX_AVAILABLE_POWER_KEY, CONF_MAX_CHARGING_CURRENT_KEY as CONF_MAX_CHARGING_CURRENT_KEY, DOMAIN as DOMAIN
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class WallboxNumberEntityDescription(NumberEntityDescription):
    min_value: float

NUMBER_TYPES: dict[str, WallboxNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxNumber(CoordinatorEntity, NumberEntity):
    entity_description: WallboxNumberEntityDescription
    coordinator: WallboxCoordinator
    _coordinator: Any
    _attr_name: Any
    _attr_min_value: Any
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxNumberEntityDescription) -> None: ...
    @property
    def max_value(self) -> float: ...
    @property
    def value(self) -> Union[float, None]: ...
    async def async_set_value(self, value: float) -> None: ...
