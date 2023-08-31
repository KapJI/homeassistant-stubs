from .const import DOMAIN as DOMAIN
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywizlight import wizlight as wizlight

class WizNumberEntityDescriptionMixin:
    value_fn: Callable[[wizlight], int | None]
    set_value_fn: Callable[[wizlight, int], Coroutine[None, None, None]]
    required_feature: str
    def __init__(self, value_fn, set_value_fn, required_feature) -> None: ...

class WizNumberEntityDescription(NumberEntityDescription, WizNumberEntityDescriptionMixin):
    def __init__(self, value_fn, set_value_fn, required_feature, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

async def _async_set_speed(device: wizlight, speed: int) -> None: ...
async def _async_set_ratio(device: wizlight, ratio: int) -> None: ...

NUMBERS: tuple[WizNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizSpeedNumber(WizEntity, NumberEntity):
    entity_description: WizNumberEntityDescription
    _attr_mode: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, wiz_data: WizData, name: str, description: WizNumberEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
