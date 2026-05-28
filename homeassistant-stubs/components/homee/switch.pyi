from . import DOMAIN as DOMAIN, HomeeConfigEntry as HomeeConfigEntry
from .const import CLIMATE_PROFILES as CLIMATE_PROFILES, LIGHT_PROFILES as LIGHT_PROFILES
from .entity import HomeeEntity as HomeeEntity
from .helpers import setup_homee_platform as setup_homee_platform
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode
from pyHomee.model_homeegram import HomeeGram as HomeeGram
from typing import Any

PARALLEL_UPDATES: int

def get_device_class(attribute: HomeeAttribute, config_entry: HomeeConfigEntry) -> SwitchDeviceClass: ...

@dataclass(frozen=True, kw_only=True)
class HomeeSwitchEntityDescription(SwitchEntityDescription):
    device_class_fn: Callable[[HomeeAttribute, HomeeConfigEntry], SwitchDeviceClass] = ...

SWITCH_DESCRIPTIONS: dict[AttributeType, HomeeSwitchEntityDescription]

async def add_switch_entities(config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, nodes: list[HomeeNode]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeSwitch(HomeeEntity, SwitchEntity):
    entity_description: HomeeSwitchEntityDescription
    _attr_name: Incomplete
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: HomeeSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def device_class(self) -> SwitchDeviceClass: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class HomeegramSwitch(SwitchEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _homeegram: Incomplete
    _entry: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_translation_key: str
    _host_connected: Incomplete
    _attr_name: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, homeegram: HomeeGram, entry: HomeeConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _on_homeegram_updated(self, homeegram: HomeeGram) -> None: ...
    async def _on_connection_changed(self, connected: bool) -> None: ...
    def _is_enabled_by_default(self, homeegram: HomeeGram) -> bool: ...
