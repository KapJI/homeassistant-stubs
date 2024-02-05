from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud import LMCloud as LaMarzoccoClient
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoNumberEntityDescription(LaMarzoccoEntityDescription, NumberEntityDescription):
    native_value_fn: Callable[[LaMarzoccoClient], float | int]
    set_value_fn: Callable[[LaMarzoccoUpdateCoordinator, float | int], Coroutine[Any, Any, bool]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, available_fn, supported_fn, native_value_fn, set_value_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoNumberEntity(LaMarzoccoEntity, NumberEntity):
    entity_description: LaMarzoccoNumberEntityDescription
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
