from . import SynoApi as SynoApi
from .const import DOMAIN as DOMAIN
from .coordinator import SynologyDSMConfigEntry as SynologyDSMConfigEntry, SynologyDSMSwitchUpdateCoordinator as SynologyDSMSwitchUpdateCoordinator
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SynologyDSMSwitchEntityDescription(SwitchEntityDescription, SynologyDSMEntityDescription): ...

SURVEILLANCE_SWITCH: tuple[SynologyDSMSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SynoDSMSurveillanceHomeModeToggle(SynologyDSMBaseEntity[SynologyDSMSwitchUpdateCoordinator], SwitchEntity):
    entity_description: SynologyDSMSwitchEntityDescription
    _version: Incomplete
    def __init__(self, api: SynoApi, version: str, coordinator: SynologyDSMSwitchUpdateCoordinator, description: SynologyDSMSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
