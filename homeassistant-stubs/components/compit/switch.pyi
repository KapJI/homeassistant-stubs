from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from compit_inext_api.consts import CompitParameter
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CompitDeviceDescription:
    name: str
    parameters: list[SwitchEntityDescription]

DESCRIPTIONS: dict[CompitParameter, SwitchEntityDescription]
DEVICE_DEFINITIONS: dict[int, CompitDeviceDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CompitSwitch(CoordinatorEntity[CompitDataUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    device_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, device_name: str, entity_description: SwitchEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
