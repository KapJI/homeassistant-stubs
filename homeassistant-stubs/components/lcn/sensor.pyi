from . import LcnEntity as LcnEntity
from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, LED_PORTS as LED_PORTS, S0_INPUTS as S0_INPUTS, SETPOINTS as SETPOINTS, THRESHOLDS as THRESHOLDS, VARIABLES as VARIABLES
from .helpers import DeviceConnectionType as DeviceConnectionType, InputType as InputType, get_device_connection as get_device_connection
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SOURCE as CONF_SOURCE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

def create_lcn_sensor_entity(hass: HomeAssistant, entity_config: ConfigType, config_entry: ConfigEntry) -> LcnEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LcnVariableSensor(LcnEntity, SensorEntity):
    variable: Any
    unit: Any
    _value: Any
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> str: ...
    def input_received(self, input_obj: InputType) -> None: ...

class LcnLedLogicSensor(LcnEntity, SensorEntity):
    source: Any
    _value: Any
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def state(self) -> Union[str, None]: ...
    def input_received(self, input_obj: InputType) -> None: ...
