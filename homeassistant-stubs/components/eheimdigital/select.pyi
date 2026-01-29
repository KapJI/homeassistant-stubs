from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from eheimdigital.classic_vario import EheimDigitalClassicVario
from eheimdigital.device import EheimDigitalDevice as EheimDigitalDevice
from eheimdigital.filter import EheimDigitalFilter
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfFrequency as UnitOfFrequency, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Literal, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EheimDigitalSelectDescription[_DeviceT: EheimDigitalDevice](SelectEntityDescription):
    options_fn: Callable[[_DeviceT], list[str]] | None = ...
    use_api_unit: Literal[True] | None = ...
    value_fn: Callable[[_DeviceT], str | None]
    set_value_fn: Callable[[_DeviceT, str], Awaitable[None] | None]

FILTER_DESCRIPTIONS: tuple[EheimDigitalSelectDescription[EheimDigitalFilter], ...]
CLASSICVARIO_DESCRIPTIONS: tuple[EheimDigitalSelectDescription[EheimDigitalClassicVario], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalSelect[_DeviceT: EheimDigitalDevice](EheimDigitalEntity[_DeviceT], SelectEntity):
    entity_description: EheimDigitalSelectDescription[_DeviceT]
    _attr_options: list[str]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT, description: EheimDigitalSelectDescription[_DeviceT]) -> None: ...
    @override
    @exception_handler
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...

class EheimDigitalFilterSelect(EheimDigitalSelect[EheimDigitalFilter]):
    entity_description: EheimDigitalSelectDescription[EheimDigitalFilter]
    _attr_native_unit_of_measurement: str | None
    _attr_options: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
