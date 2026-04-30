from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from sfrbox_api.bridge import SFRBox as SFRBox
from sfrbox_api.models import DslInfo as DslInfo, FtthInfo as FtthInfo, SystemInfo as SystemInfo, VoipInfo as VoipInfo, WanInfo as WanInfo
from typing import Any

_LOGGER: Incomplete
_SCAN_INTERVAL: Incomplete
type SFRConfigEntry = ConfigEntry[SFRRuntimeData]

@dataclass
class SFRRuntimeData:
    box: SFRBox
    has_authentication: bool
    dsl: SFRDataUpdateCoordinator[DslInfo]
    ftth: SFRDataUpdateCoordinator[FtthInfo]
    system: SFRDataUpdateCoordinator[SystemInfo]
    voip: SFRDataUpdateCoordinator[VoipInfo] | None
    wan: SFRDataUpdateCoordinator[WanInfo]

class SFRDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT]):
    config_entry: SFRConfigEntry
    box: Incomplete
    _method: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SFRConfigEntry, box: SFRBox, name: str, method: Callable[[SFRBox], Coroutine[Any, Any, _DataT | None]]) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
