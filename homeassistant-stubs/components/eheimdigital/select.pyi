from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from eheimdigital.classic_vario import EheimDigitalClassicVario
from eheimdigital.device import EheimDigitalDevice
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Generic, TypeVar, override

PARALLEL_UPDATES: int
_DeviceT_co = TypeVar('_DeviceT_co', bound=EheimDigitalDevice, covariant=True)

@dataclass(frozen=True, kw_only=True)
class EheimDigitalSelectDescription(SelectEntityDescription, Generic[_DeviceT_co]):
    value_fn: Callable[[_DeviceT_co], str | None]
    set_value_fn: Callable[[_DeviceT_co, str], Awaitable[None]]

CLASSICVARIO_DESCRIPTIONS: tuple[EheimDigitalSelectDescription[EheimDigitalClassicVario], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalSelect(EheimDigitalEntity[_DeviceT_co], SelectEntity, Generic[_DeviceT_co]):
    entity_description: EheimDigitalSelectDescription[_DeviceT_co]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT_co, description: EheimDigitalSelectDescription[_DeviceT_co]) -> None: ...
    @override
    @exception_handler
    async def async_select_option(self, option: str) -> None: ...
    _attr_current_option: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
