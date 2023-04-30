from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

class OverkizSwitchDescriptionMixin:
    turn_on: str
    turn_off: str
    def __init__(self, turn_on, turn_off) -> None: ...

class OverkizSwitchDescription(SwitchEntityDescription, OverkizSwitchDescriptionMixin):
    is_on: Callable[[Callable[[str], OverkizStateType]], bool] | None
    turn_on_args: OverkizStateType | list[OverkizStateType] | None
    turn_off_args: OverkizStateType | list[OverkizStateType] | None
    def __init__(self, turn_on, turn_off, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, is_on, turn_on_args, turn_off_args) -> None: ...

SWITCH_DESCRIPTIONS: list[OverkizSwitchDescription]
SUPPORTED_DEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizSwitch(OverkizDescriptiveEntity, SwitchEntity):
    entity_description: OverkizSwitchDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
