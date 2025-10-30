from .const import API_NONE_VALUE as API_NONE_VALUE
from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from .entity import VolvoEntity as VolvoEntity, VolvoEntityDescription as VolvoEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from volvocarsapi.models import VolvoCarsApiBaseModel as VolvoCarsApiBaseModel

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VolvoBinarySensorDescription(BinarySensorEntityDescription, VolvoEntityDescription):
    on_values: tuple[str, ...]

@dataclass(frozen=True, kw_only=True)
class VolvoCarsDoorDescription(VolvoBinarySensorDescription):
    device_class: BinarySensorDeviceClass = ...
    on_values: tuple[str, ...] = field(default=('OPEN', 'AJAR'), init=False)

@dataclass(frozen=True, kw_only=True)
class VolvoCarsTireDescription(VolvoBinarySensorDescription):
    device_class: BinarySensorDeviceClass = ...
    on_values: tuple[str, ...] = field(default=('VERY_LOW_PRESSURE', 'LOW_PRESSURE', 'HIGH_PRESSURE'), init=False)

@dataclass(frozen=True, kw_only=True)
class VolvoCarsWindowDescription(VolvoBinarySensorDescription):
    device_class: BinarySensorDeviceClass = ...
    on_values: tuple[str, ...] = field(default=('OPEN', 'AJAR'), init=False)

_DESCRIPTIONS: tuple[VolvoBinarySensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VolvoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VolvoBinarySensor(VolvoEntity, BinarySensorEntity):
    entity_description: VolvoBinarySensorDescription
    _attr_is_on: Incomplete
    def _update_state(self, api_field: VolvoCarsApiBaseModel | None) -> None: ...
