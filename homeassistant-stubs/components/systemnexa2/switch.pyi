from .coordinator import SystemNexa2ConfigEntry as SystemNexa2ConfigEntry, SystemNexa2DataUpdateCoordinator as SystemNexa2DataUpdateCoordinator
from .entity import SystemNexa2Entity as SystemNexa2Entity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from sn2.device import OnOffSetting as OnOffSetting
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SystemNexa2SwitchEntityDescription(SwitchEntityDescription): ...

SWITCH_TYPES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: SystemNexa2ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SystemNexa2ConfigurationSwitch(SystemNexa2Entity, SwitchEntity):
    _attr_device_class: Incomplete
    entity_description: SystemNexa2SwitchEntityDescription
    _setting: Incomplete
    def __init__(self, coordinator: SystemNexa2DataUpdateCoordinator, description: SystemNexa2SwitchEntityDescription, setting: OnOffSetting) -> None: ...
    async def async_turn_on(self, **_kwargs: Any) -> None: ...
    async def async_turn_off(self, **_kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...

class SystemNexa2SwitchPlug(SystemNexa2Entity, SwitchEntity):
    _attr_translation_key: str
    def __init__(self, coordinator: SystemNexa2DataUpdateCoordinator) -> None: ...
    async def async_turn_on(self, **_kwargs: Any) -> None: ...
    async def async_turn_off(self, **_kwargs: Any) -> None: ...
    async def async_toggle(self, **_kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
