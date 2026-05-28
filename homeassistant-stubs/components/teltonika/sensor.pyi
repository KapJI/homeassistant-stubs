from . import TeltonikaConfigEntry as TeltonikaConfigEntry, TeltonikaDataUpdateCoordinator as TeltonikaDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from teltasync.modems import ModemStatusFull as ModemStatusFull

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TeltonikaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[ModemStatusFull], StateType]

SENSOR_DESCRIPTIONS: tuple[TeltonikaSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeltonikaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeltonikaSensorEntity(CoordinatorEntity[TeltonikaDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: TeltonikaSensorEntityDescription
    _modem_id: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _modem_name: Incomplete
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: TeltonikaDataUpdateCoordinator, device_info: DeviceInfo, description: TeltonikaSensorEntityDescription, modem_id: str, modem: ModemStatusFull) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
