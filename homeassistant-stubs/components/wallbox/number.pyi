from . import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator, WallboxEntity as WallboxEntity
from .const import CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_MAX_AVAILABLE_POWER_KEY as CHARGER_MAX_AVAILABLE_POWER_KEY, CHARGER_MAX_CHARGING_CURRENT_KEY as CHARGER_MAX_CHARGING_CURRENT_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, DOMAIN as DOMAIN
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class WallboxNumberEntityDescription(NumberEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, max_value, min_value, step) -> None: ...

NUMBER_TYPES: dict[str, WallboxNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxNumber(WallboxEntity, NumberEntity):
    entity_description: WallboxNumberEntityDescription
    _coordinator: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxNumberEntityDescription) -> None: ...
    @property
    def max_value(self) -> float: ...
    @property
    def value(self) -> Union[float, None]: ...
    async def async_set_value(self, value: float) -> None: ...
