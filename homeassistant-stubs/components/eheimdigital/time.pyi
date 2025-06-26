from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from datetime import time
from eheimdigital.classic_vario import EheimDigitalClassicVario
from eheimdigital.device import EheimDigitalDevice as EheimDigitalDevice
from eheimdigital.heater import EheimDigitalHeater
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EheimDigitalTimeDescription[_DeviceT: EheimDigitalDevice](TimeEntityDescription):
    value_fn: Callable[[_DeviceT], time | None]
    set_value_fn: Callable[[_DeviceT, time], Awaitable[None]]

CLASSICVARIO_DESCRIPTIONS: tuple[EheimDigitalTimeDescription[EheimDigitalClassicVario], ...]
HEATER_DESCRIPTIONS: tuple[EheimDigitalTimeDescription[EheimDigitalHeater], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalTime[_DeviceT: EheimDigitalDevice](EheimDigitalEntity[_DeviceT], TimeEntity):
    entity_description: EheimDigitalTimeDescription[_DeviceT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT, description: EheimDigitalTimeDescription[_DeviceT]) -> None: ...
    @override
    @exception_handler
    async def async_set_value(self, value: time) -> None: ...
    _attr_native_value: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
