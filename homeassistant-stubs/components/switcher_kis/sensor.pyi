from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .entity import SwitcherEntity as SwitcherEntity
from _typeshed import Incomplete
from aioswitcher.device import SwitcherBase as SwitcherBase
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class SwitcherSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SwitcherBase], StateType]

POWER_SENSORS: list[SwitcherSensorEntityDescription]
TIME_SENSORS: list[SwitcherSensorEntityDescription]
TEMPERATURE_SENSORS: list[SwitcherSensorEntityDescription]
POWER_PLUG_SENSORS = POWER_SENSORS
WATER_HEATER_SENSORS: Incomplete
THERMOSTAT_SENSORS = TEMPERATURE_SENSORS

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitcherSensorEntity(SwitcherEntity, SensorEntity):
    entity_description: SwitcherSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, description: SwitcherSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
