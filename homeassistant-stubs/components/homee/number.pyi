from . import HomeeConfigEntry as HomeeConfigEntry
from .const import HOMEE_UNIT_TO_HA_UNIT as HOMEE_UNIT_TO_HA_UNIT
from .entity import HomeeEntity as HomeeEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.model import HomeeAttribute as HomeeAttribute

PARALLEL_UPDATES: int
NUMBER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeNumber(HomeeEntity, NumberEntity):
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: NumberEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> int: ...
    async def async_set_native_value(self, value: float) -> None: ...
