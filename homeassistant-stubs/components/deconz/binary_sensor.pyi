from .const import ATTR_DARK as ATTR_DARK, ATTR_ON as ATTR_ON
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from .util import serial_from_unique_id as serial_from_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from pydeconz.models.sensor.alarm import Alarm
from pydeconz.models.sensor.carbon_monoxide import CarbonMonoxide
from pydeconz.models.sensor.fire import Fire
from pydeconz.models.sensor.generic_flag import GenericFlag
from pydeconz.models.sensor.open_close import OpenClose
from pydeconz.models.sensor.presence import Presence
from pydeconz.models.sensor.vibration import Vibration
from pydeconz.models.sensor.water import Water
from typing import Generic, TypeVar

_SensorDeviceT = TypeVar('_SensorDeviceT', bound=PydeconzSensorBase)
ATTR_ORIENTATION: str
ATTR_TILTANGLE: str
ATTR_VIBRATIONSTRENGTH: str
PROVIDES_EXTRA_ATTRIBUTES: Incomplete
T = TypeVar('T', Alarm, CarbonMonoxide, Fire, GenericFlag, OpenClose, Presence, Vibration, Water, PydeconzSensorBase)

@dataclass
class DeconzBinarySensorDescriptionMixin(Generic[T]):
    update_key: str
    value_fn: Callable[[T], bool | None]
    def __init__(self, update_key, value_fn) -> None: ...

@dataclass
class DeconzBinarySensorDescription(BinarySensorEntityDescription, DeconzBinarySensorDescriptionMixin[T]):
    instance_check: type[T] | None = ...
    name_suffix: str = ...
    old_unique_id_suffix: str = ...
    def __init__(self, update_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, instance_check, name_suffix, old_unique_id_suffix) -> None: ...

ENTITY_DESCRIPTIONS: tuple[DeconzBinarySensorDescription, ...]

def async_update_unique_id(hass: HomeAssistant, unique_id: str, description: DeconzBinarySensorDescription) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzBinarySensor(DeconzDevice[SensorResources], BinarySensorEntity):
    TYPE = DOMAIN
    entity_description: DeconzBinarySensorDescription
    unique_id_suffix: Incomplete
    _update_key: Incomplete
    _name_suffix: Incomplete
    def __init__(self, device: SensorResources, gateway: DeconzGateway, description: DeconzBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool | float | int | list | None]: ...
