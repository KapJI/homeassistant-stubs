from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA
from .entity import LcnEntity as LcnEntity
from .helpers import InputType as InputType, LcnConfigEntry as LcnConfigEntry
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES, CONF_SOURCE as CONF_SOURCE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

def add_lcn_entities(config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, entity_configs: Iterable[ConfigType]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: LcnConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LcnBinarySensor(LcnEntity, BinarySensorEntity):
    bin_sensor_port: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    _attr_available: Incomplete
    async def async_update(self) -> None: ...
    _attr_is_on: Incomplete
    def input_received(self, input_obj: InputType) -> None: ...
