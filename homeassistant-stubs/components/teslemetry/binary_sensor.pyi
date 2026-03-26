from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .const import TeslemetryState as TeslemetryState
from .entity import TeslemetryEnergyInfoEntity as TeslemetryEnergyInfoEntity, TeslemetryEnergyLiveEntity as TeslemetryEnergyLiveEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import StateType as StateType
from teslemetry_stream.vehicle import TeslemetryStreamVehicle as TeslemetryStreamVehicle

PARALLEL_UPDATES: int
WINDOW_STATES: Incomplete

@dataclass(frozen=True, kw_only=True)
class TeslemetryBinarySensorEntityDescription(BinarySensorEntityDescription):
    polling_value_fn: Callable[[StateType], bool | None] = ...
    polling: bool = ...
    streaming_listener: Callable[[TeslemetryStreamVehicle, Callable[[bool | None], None]], Callable[[], None]] | None = ...
    streaming_firmware: str = ...

VEHICLE_DESCRIPTIONS: tuple[TeslemetryBinarySensorEntityDescription, ...]
ENERGY_LIVE_DESCRIPTIONS: tuple[TeslemetryBinarySensorEntityDescription, ...]
ENERGY_INFO_DESCRIPTIONS: tuple[TeslemetryBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryVehiclePollingBinarySensorEntity(TeslemetryVehiclePollingEntity, BinarySensorEntity):
    entity_description: TeslemetryBinarySensorEntityDescription
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryBinarySensorEntityDescription) -> None: ...
    _attr_available: Incomplete
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryVehicleStreamingBinarySensorEntity(TeslemetryVehicleStreamEntity, BinarySensorEntity, RestoreEntity):
    entity_description: TeslemetryBinarySensorEntityDescription
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryBinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    _attr_available: Incomplete
    def _async_value_from_stream(self, value: bool | None) -> None: ...

class TeslemetryEnergyLiveBinarySensorEntity(TeslemetryEnergyLiveEntity, BinarySensorEntity):
    entity_description: TeslemetryBinarySensorEntityDescription
    def __init__(self, data: TeslemetryEnergyData, description: TeslemetryBinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryEnergyInfoBinarySensorEntity(TeslemetryEnergyInfoEntity, BinarySensorEntity):
    entity_description: TeslemetryBinarySensorEntityDescription
    def __init__(self, data: TeslemetryEnergyData, description: TeslemetryBinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
