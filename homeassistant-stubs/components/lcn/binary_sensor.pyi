from .const import BINSENSOR_PORTS as BINSENSOR_PORTS, CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, DOMAIN as DOMAIN, SETPOINTS as SETPOINTS
from .entity import LcnEntity as LcnEntity
from .helpers import InputType as InputType, LcnConfigEntry as LcnConfigEntry
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SOURCE as CONF_SOURCE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

PARALLEL_UPDATES: int

def add_lcn_entities(config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, entity_configs: Iterable[ConfigType]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LcnRegulatorLockSensor(LcnEntity, BinarySensorEntity):
    setpoint_variable: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_is_on: Incomplete
    def input_received(self, input_obj: InputType) -> None: ...

class LcnBinarySensor(LcnEntity, BinarySensorEntity):
    bin_sensor_port: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_is_on: Incomplete
    def input_received(self, input_obj: InputType) -> None: ...

class LcnLockKeysSensor(LcnEntity, BinarySensorEntity):
    source: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _attr_is_on: Incomplete
    def input_received(self, input_obj: InputType) -> None: ...
