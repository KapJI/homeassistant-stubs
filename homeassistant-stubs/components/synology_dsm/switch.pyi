from . import SynoApi as SynoApi, SynologyDSMBaseEntity as SynologyDSMBaseEntity
from .const import COORDINATOR_SWITCHES as COORDINATOR_SWITCHES, DOMAIN as DOMAIN, SURVEILLANCE_SWITCH as SURVEILLANCE_SWITCH, SYNO_API as SYNO_API, SynologyDSMSwitchEntityDescription as SynologyDSMSwitchEntityDescription
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMSurveillanceHomeModeToggle(SynologyDSMBaseEntity, SwitchEntity):
    coordinator: DataUpdateCoordinator[dict[str, dict[str, bool]]]
    entity_description: SynologyDSMSwitchEntityDescription
    _version: Any
    def __init__(self, api: SynoApi, version: str, coordinator: DataUpdateCoordinator[dict[str, dict[str, bool]]], description: SynologyDSMSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
