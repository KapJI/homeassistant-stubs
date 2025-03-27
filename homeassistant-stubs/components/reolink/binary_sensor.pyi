from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkEntityDescription as ReolinkEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from reolink_aio.api import Host as Host

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkBinarySensorEntityDescription(BinarySensorEntityDescription, ReolinkChannelEntityDescription):
    value: Callable[[Host, int], bool]

@dataclass(frozen=True, kw_only=True)
class ReolinkSmartAIBinarySensorEntityDescription(BinarySensorEntityDescription, ReolinkEntityDescription):
    smart_type: str
    value: Callable[[Host, int, int], bool]
    supported: Callable[[Host, int, int], bool] = ...

BINARY_PUSH_SENSORS: Incomplete
BINARY_SENSORS: Incomplete
BINARY_SMART_AI_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ReolinkBinarySensorEntity(ReolinkChannelCoordinatorEntity, BinarySensorEntity):
    entity_description: ReolinkBinarySensorEntityDescription
    _attr_translation_key: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class ReolinkPushBinarySensorEntity(ReolinkBinarySensorEntity):
    async def async_added_to_hass(self) -> None: ...
    async def _async_handle_event(self, event: str) -> None: ...

class ReolinkSmartAIBinarySensorEntity(ReolinkChannelCoordinatorEntity, BinarySensorEntity):
    entity_description: ReolinkSmartAIBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    _location: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, location: int, entity_description: ReolinkSmartAIBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
