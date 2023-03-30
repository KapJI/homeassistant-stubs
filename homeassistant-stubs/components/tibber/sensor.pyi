import tibber
from .const import MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.recorder.models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData
from homeassistant.components.recorder.statistics import async_add_external_statistics as async_add_external_statistics, get_last_statistics as get_last_statistics, statistics_during_period as statistics_during_period
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import Throttle as Throttle
from typing import Any

_LOGGER: Incomplete
ICON: str
SCAN_INTERVAL: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete
PARALLEL_UPDATES: int
RT_SENSORS: tuple[SensorEntityDescription, ...]
SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TibberSensor(SensorEntity):
    _tibber_home: Incomplete
    _home_name: Incomplete
    _device_name: Incomplete
    _model: Incomplete
    def __init__(self, *args: Any, tibber_home: tibber.TibberHome, **kwargs: Any) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...

class TibberSensorElPrice(TibberSensor):
    _last_updated: Incomplete
    _spread_load_constant: Incomplete
    _attr_available: bool
    _attr_extra_state_attributes: Incomplete
    _attr_icon: Incomplete
    _attr_name: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _model: str
    _device_name: Incomplete
    def __init__(self, tibber_home: tibber.TibberHome) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    async def async_update(self) -> None: ...
    async def _fetch_data(self) -> None: ...

class TibberDataSensor(TibberSensor, CoordinatorEntity['TibberDataCoordinator']):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _device_name: Incomplete
    def __init__(self, tibber_home: tibber.TibberHome, coordinator: TibberDataCoordinator, entity_description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class TibberSensorRT(TibberSensor, CoordinatorEntity['TibberRtDataCoordinator']):
    entity_description: Incomplete
    _model: str
    _device_name: Incomplete
    _attr_name: Incomplete
    _attr_native_value: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, tibber_home: tibber.TibberHome, description: SensorEntityDescription, initial_state: float, coordinator: TibberRtDataCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_last_reset: Incomplete
    def _handle_coordinator_update(self) -> None: ...

class TibberRtDataCoordinator(DataUpdateCoordinator):
    _async_add_entities: Incomplete
    _tibber_home: Incomplete
    hass: Incomplete
    _added_sensors: Incomplete
    _async_remove_device_updates_handler: Incomplete
    def __init__(self, async_add_entities: AddEntitiesCallback, tibber_home: tibber.TibberHome, hass: HomeAssistant) -> None: ...
    def _handle_ha_stop(self, _event: Event) -> None: ...
    def _add_sensors(self) -> None: ...
    def get_live_measurement(self) -> Any: ...

class TibberDataCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    _tibber_connection: Incomplete
    def __init__(self, hass: HomeAssistant, tibber_connection: tibber.Tibber) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _insert_statistics(self) -> None: ...
