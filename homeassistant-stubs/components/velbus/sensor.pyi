from . import VelbusConfigEntry as VelbusConfigEntry
from .entity import VelbusEntity as VelbusEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from velbusaio.channels import ButtonCounter, LightSensor, SensorNumber, Temperature

PARALLEL_UPDATES: int
type VelbusSensorChannel = ButtonCounter | Temperature | LightSensor | SensorNumber

@dataclass(frozen=True, kw_only=True)
class VelbusSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[VelbusSensorChannel], float | None] = ...
    unit_fn: Callable[[VelbusSensorChannel], str | None] = ...
    unique_id_suffix: str = ...

SENSOR_DESCRIPTIONS: dict[str, VelbusSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: VelbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VelbusSensor(VelbusEntity, SensorEntity):
    _channel: VelbusSensorChannel
    entity_description: VelbusSensorEntityDescription
    _is_counter: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, channel: VelbusSensorChannel, description: VelbusSensorEntityDescription, is_counter: bool = False) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
