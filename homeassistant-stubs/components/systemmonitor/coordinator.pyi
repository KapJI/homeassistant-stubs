import abc
import psutil
from _typeshed import Incomplete
from abc import abstractmethod
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from psutil._common import sdiskusage, shwtemp, snetio, snicaddr, sswap
from typing import NamedTuple, TypeVar

_LOGGER: Incomplete

class VirtualMemory(NamedTuple):
    total: float
    available: float
    percent: float
    used: float
    free: float
dataT = TypeVar('dataT', bound=datetime | dict[str, list[shwtemp]] | dict[str, list[snicaddr]] | dict[str, snetio] | float | list[psutil.Process] | sswap | VirtualMemory | tuple[float, float, float] | sdiskusage | None)

class MonitorCoordinator(DataUpdateCoordinator[dataT], metaclass=abc.ABCMeta):
    def __init__(self, hass: HomeAssistant, name: str) -> None: ...
    async def _async_update_data(self) -> dataT: ...
    @abstractmethod
    def update_data(self) -> dataT: ...

class SystemMonitorDiskCoordinator(MonitorCoordinator[sdiskusage]):
    _argument: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, argument: str) -> None: ...
    def update_data(self) -> sdiskusage: ...

class SystemMonitorSwapCoordinator(MonitorCoordinator[sswap]):
    def update_data(self) -> sswap: ...

class SystemMonitorMemoryCoordinator(MonitorCoordinator[VirtualMemory]):
    def update_data(self) -> VirtualMemory: ...

class SystemMonitorNetIOCoordinator(MonitorCoordinator[dict[str, snetio]]):
    def update_data(self) -> dict[str, snetio]: ...

class SystemMonitorNetAddrCoordinator(MonitorCoordinator[dict[str, list[snicaddr]]]):
    def update_data(self) -> dict[str, list[snicaddr]]: ...

class SystemMonitorLoadCoordinator(MonitorCoordinator[tuple[float, float, float]]):
    def update_data(self) -> tuple[float, float, float]: ...

class SystemMonitorProcessorCoordinator(MonitorCoordinator[float | None]):
    def update_data(self) -> float | None: ...

class SystemMonitorBootTimeCoordinator(MonitorCoordinator[datetime]):
    def update_data(self) -> datetime: ...

class SystemMonitorProcessCoordinator(MonitorCoordinator[list[psutil.Process]]):
    def update_data(self) -> list[psutil.Process]: ...

class SystemMonitorCPUtempCoordinator(MonitorCoordinator[dict[str, list[shwtemp]]]):
    def update_data(self) -> dict[str, list[shwtemp]]: ...
