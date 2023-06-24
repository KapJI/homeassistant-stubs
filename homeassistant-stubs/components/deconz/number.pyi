from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from .util import serial_from_unique_id as serial_from_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.number import DOMAIN as DOMAIN, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.gateway import DeconzSession as DeconzSession
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from pydeconz.models.sensor.presence import Presence
from typing import Any, Generic, TypeVar

T = TypeVar('T', Presence, PydeconzSensorBase)

class DeconzNumberDescriptionMixin(Generic[T]):
    instance_check: type[T]
    name_suffix: str
    set_fn: Callable[[DeconzSession, str, int], Coroutine[Any, Any, dict[str, Any]]]
    update_key: str
    value_fn: Callable[[T], float | None]
    def __init__(self, instance_check, name_suffix, set_fn, update_key, value_fn) -> None: ...

class DeconzNumberDescription(NumberEntityDescription, DeconzNumberDescriptionMixin[T]):
    def __init__(self, instance_check, name_suffix, set_fn, update_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

ENTITY_DESCRIPTIONS: tuple[DeconzNumberDescription, ...]

def async_update_unique_id(hass: HomeAssistant, unique_id: str, description: DeconzNumberDescription) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzNumber(DeconzDevice[SensorResources], NumberEntity):
    TYPE = DOMAIN
    entity_description: DeconzNumberDescription
    unique_id_suffix: Incomplete
    _name_suffix: Incomplete
    _update_key: Incomplete
    def __init__(self, device: SensorResources, gateway: DeconzGateway, description: DeconzNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
