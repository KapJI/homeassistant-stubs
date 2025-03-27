from . import HomeeConfigEntry as HomeeConfigEntry
from .const import CLIMATE_PROFILES as CLIMATE_PROFILES, LIGHT_PROFILES as LIGHT_PROFILES
from .entity import HomeeEntity as HomeeEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute
from typing import Any

PARALLEL_UPDATES: int

def get_device_class(attribute: HomeeAttribute, config_entry: HomeeConfigEntry) -> SwitchDeviceClass: ...

@dataclass(frozen=True, kw_only=True)
class HomeeSwitchEntityDescription(SwitchEntityDescription):
    device_class_fn: Callable[[HomeeAttribute, HomeeConfigEntry], SwitchDeviceClass] = ...

SWITCH_DESCRIPTIONS: dict[AttributeType, HomeeSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

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
