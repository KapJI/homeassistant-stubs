from .entity import LyngdorfEntity as LyngdorfEntity
from .models import LyngdorfConfigEntry as LyngdorfConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfSoundPressure as UnitOfSoundPressure
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LyngdorfSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[LyngdorfReceiver], str | float | None]
    options_fn: Callable[[LyngdorfReceiver], list[str]] | None = ...

def _known(value: str | None, options: list[str]) -> str | None: ...

MAIN_ZONE_SENSORS: tuple[LyngdorfSensorEntityDescription, ...]
ZONE_B_SENSORS: tuple[LyngdorfSensorEntityDescription, ...]
MAXIMUM_VOLUME_SENSOR: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: LyngdorfConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LyngdorfSensor(LyngdorfEntity, SensorEntity):
    entity_description: LyngdorfSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, receiver: LyngdorfReceiver, config_entry: LyngdorfConfigEntry, device_info: DeviceInfo, description: LyngdorfSensorEntityDescription) -> None: ...
    @override
    @property
    def options(self) -> list[str] | None: ...
    @override
    @property
    def native_value(self) -> str | float | None: ...
