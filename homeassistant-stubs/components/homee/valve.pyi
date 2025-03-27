from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeEntity as HomeeEntity
from _typeshed import Incomplete
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.model import HomeeAttribute as HomeeAttribute

PARALLEL_UPDATES: int
VALVE_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeValve(HomeeEntity, ValveEntity):
    _attr_reports_position: bool
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: ValveEntityDescription) -> None: ...
    @property
    def supported_features(self) -> ValveEntityFeature: ...
    @property
    def current_valve_position(self) -> int | None: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_set_valve_position(self, position: int) -> None: ...
