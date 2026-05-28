from .coordinator import CentriConnectConfigEntry as CentriConnectConfigEntry, CentriConnectCoordinator as CentriConnectCoordinator
from .entity import CentriConnectBaseEntity as CentriConnectBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType, UnitOfTemperature as UnitOfTemperature
from homeassistant.const import PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfLength as UnitOfLength, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
_ALERT_STATUS_VALUES: Incomplete

class CentriConnectSensorType(StrEnum):
    ALERT_STATUS = 'alert_status'
    ALTITUDE = 'altitude'
    BATTERY_LEVEL = 'battery_level'
    BATTERY_VOLTAGE = 'battery_voltage'
    DEVICE_TEMPERATURE = 'device_temperature'
    LAST_POST_TIME = 'last_post_time'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    LTE_SIGNAL_LEVEL = 'lte_signal_level'
    LTE_SIGNAL_STRENGTH = 'lte_signal_strength'
    NEXT_POST_TIME = 'next_post_time'
    SOLAR_LEVEL = 'solar_level'
    SOLAR_VOLTAGE = 'solar_voltage'
    TANK_LEVEL = 'tank_level'
    TANK_REMAINING_VOLUME = 'tank_remaining_volume'
    TANK_SIZE = 'tank_size'

@dataclass(frozen=True, kw_only=True)
class CentriConnectSensorEntityDescription(SensorEntityDescription):
    key: CentriConnectSensorType
    value_fn: Callable[[CentriConnectCoordinator], StateType | datetime | None]

ENTITIES: tuple[CentriConnectSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: CentriConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CentriConnectSensor(CentriConnectBaseEntity, SensorEntity):
    entity_description: CentriConnectSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime | None: ...
