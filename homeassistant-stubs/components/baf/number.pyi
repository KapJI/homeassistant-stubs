from .const import DOMAIN as DOMAIN, HALF_DAY_SECS as HALF_DAY_SECS, ONE_DAY_SECS as ONE_DAY_SECS, ONE_MIN_SECS as ONE_MIN_SECS, SPEED_RANGE as SPEED_RANGE
from .entity import BAFEntity as BAFEntity
from .models import BAFData as BAFData
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class BAFNumberDescriptionMixin:
    value_fn: Callable[[Device], Union[int, None]]
    mode: NumberMode
    def __init__(self, value_fn, mode) -> None: ...

class BAFNumberDescription(NumberEntityDescription, BAFNumberDescriptionMixin):
    def __init__(self, value_fn, mode, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, max_value, min_value, native_max_value, native_min_value, native_unit_of_measurement, native_step, step) -> None: ...

AUTO_COMFORT_NUMBER_DESCRIPTIONS: Incomplete
FAN_NUMBER_DESCRIPTIONS: Incomplete
LIGHT_NUMBER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFNumber(BAFEntity, NumberEntity):
    entity_description: BAFNumberDescription
    _attr_unique_id: Incomplete
    _attr_mode: Incomplete
    def __init__(self, device: Device, description: BAFNumberDescription) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
