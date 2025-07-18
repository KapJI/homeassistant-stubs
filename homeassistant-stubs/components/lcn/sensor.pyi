from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, LED_PORTS as LED_PORTS, S0_INPUTS as S0_INPUTS, SETPOINTS as SETPOINTS, THRESHOLDS as THRESHOLDS, VARIABLES as VARIABLES
from .entity import LcnEntity as LcnEntity
from .helpers import InputType as InputType, LcnConfigEntry as LcnConfigEntry
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SOURCE as CONF_SOURCE, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, LIGHT_LUX as LIGHT_LUX, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

PARALLEL_UPDATES: int
DEVICE_CLASS_MAPPING: Incomplete
UNIT_OF_MEASUREMENT_MAPPING: Incomplete

def add_lcn_entities(config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, entity_configs: Iterable[ConfigType]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LcnVariableSensor(LcnEntity, SensorEntity):
    variable: Incomplete
    unit: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def input_received(self, input_obj: InputType) -> None: ...

class LcnLedLogicSensor(LcnEntity, SensorEntity):
    source: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_native_value: Incomplete
    def input_received(self, input_obj: InputType) -> None: ...
