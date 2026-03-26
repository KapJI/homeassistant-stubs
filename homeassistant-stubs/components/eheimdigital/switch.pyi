from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from eheimdigital.classic_vario import EheimDigitalClassicVario
from eheimdigital.device import EheimDigitalDevice as EheimDigitalDevice
from eheimdigital.filter import EheimDigitalFilter
from eheimdigital.reeflex import EheimDigitalReeflexUV
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EheimDigitalSwitchDescription[_DeviceT: EheimDigitalDevice](SwitchEntityDescription):
    is_on_fn: Callable[[_DeviceT], bool]
    set_fn: Callable[[_DeviceT, bool], Awaitable[None]]

REEFLEX_DESCRIPTIONS: tuple[EheimDigitalSwitchDescription[EheimDigitalReeflexUV], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalSwitch[_DeviceT: EheimDigitalDevice](EheimDigitalEntity[_DeviceT], SwitchEntity):
    entity_description: EheimDigitalSwitchDescription[_DeviceT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT, description: EheimDigitalSwitchDescription[_DeviceT]) -> None: ...
    @exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...

class EheimDigitalFilterSwitch(EheimDigitalEntity[EheimDigitalClassicVario | EheimDigitalFilter], SwitchEntity):
    _attr_translation_key: str
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: EheimDigitalClassicVario | EheimDigitalFilter) -> None: ...
    @override
    @exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    @exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
