from . import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator, WallboxEntity as WallboxEntity
from .const import BIDIRECTIONAL_MODEL_PREFIXES as BIDIRECTIONAL_MODEL_PREFIXES, CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_MAX_AVAILABLE_POWER_KEY as CHARGER_MAX_AVAILABLE_POWER_KEY, CHARGER_MAX_CHARGING_CURRENT_KEY as CHARGER_MAX_CHARGING_CURRENT_KEY, CHARGER_PART_NUMBER_KEY as CHARGER_PART_NUMBER_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class WallboxNumberEntityDescription(NumberEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

NUMBER_TYPES: dict[str, WallboxNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxNumber(WallboxEntity, NumberEntity):
    entity_description: WallboxNumberEntityDescription
    _coordinator: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _is_bidirectional: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: WallboxNumberEntityDescription) -> None: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
