from .const import CONF_CALIBRATION_FACTOR as CONF_CALIBRATION_FACTOR, CONF_INDOOR_HUMIDITY as CONF_INDOOR_HUMIDITY, CONF_INDOOR_TEMP as CONF_INDOOR_TEMP, CONF_OUTDOOR_TEMP as CONF_OUTDOOR_TEMP, DEFAULT_NAME as DEFAULT_NAME
from _typeshed import Incomplete
from homeassistant import util as util
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, PERCENTAGE as PERCENTAGE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.device import async_device_info_to_link_from_entity as async_device_info_to_link_from_entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

_LOGGER: Incomplete
ATTR_CRITICAL_TEMP: str
ATTR_DEWPOINT: str
MAGNUS_K2: float
MAGNUS_K3: float
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MoldIndicator(SensorEntity):
    _attr_should_poll: bool
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _state: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _indoor_temp_sensor: Incomplete
    _indoor_humidity_sensor: Incomplete
    _outdoor_temp_sensor: Incomplete
    _calib_factor: Incomplete
    _is_metric: Incomplete
    _attr_available: bool
    _entities: Incomplete
    _dewpoint: Incomplete
    _indoor_temp: Incomplete
    _outdoor_temp: Incomplete
    _indoor_hum: Incomplete
    _crit_temp: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, is_metric: bool, indoor_temp_sensor: str, outdoor_temp_sensor: str, indoor_humidity_sensor: str, calib_factor: float, unique_id: str | None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_sensor(self, entity: str, old_state: State | None, new_state: State | None) -> bool: ...
    @staticmethod
    def _update_temp_sensor(state: State) -> float | None: ...
    @staticmethod
    def _update_hum_sensor(state: State) -> float | None: ...
    async def async_update(self) -> None: ...
    def _calc_dewpoint(self) -> None: ...
    def _calc_moldindicator(self) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
