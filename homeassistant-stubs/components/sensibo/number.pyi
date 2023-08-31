from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice
from typing import Any

PARALLEL_UPDATES: int

class SensiboEntityDescriptionMixin:
    remote_key: str
    value_fn: Callable[[SensiboDevice], float | None]
    def __init__(self, remote_key, value_fn) -> None: ...

class SensiboNumberEntityDescription(NumberEntityDescription, SensiboEntityDescriptionMixin):
    def __init__(self, remote_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

DEVICE_NUMBER_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboNumber(SensiboDeviceBaseEntity, NumberEntity):
    entity_description: SensiboNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    async def async_send_api_call(self, key: str, value: Any) -> bool: ...
