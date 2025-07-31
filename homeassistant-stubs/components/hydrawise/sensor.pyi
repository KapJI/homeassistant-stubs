from .coordinator import HydrawiseConfigEntry as HydrawiseConfigEntry
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pydrawise.schema import Controller as Controller, ControllerWaterUseSummary, Zone as Zone
from typing import Any

@dataclass(frozen=True, kw_only=True)
class HydrawiseSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[HydrawiseSensor], Any]

def _get_water_use(sensor: HydrawiseSensor) -> ControllerWaterUseSummary: ...

WATER_USE_CONTROLLER_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
WATER_USE_ZONE_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
FLOW_CONTROLLER_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
FLOW_ZONE_SENSORS: tuple[SensorEntityDescription, ...]
ZONE_SENSORS: tuple[HydrawiseSensorEntityDescription, ...]
FLOW_MEASUREMENT_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HydrawiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HydrawiseSensor(HydrawiseEntity, SensorEntity):
    entity_description: HydrawiseSensorEntityDescription
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def icon(self) -> str | None: ...
    _attr_native_value: Incomplete
    def _update_attrs(self) -> None: ...
