from .const import A01_UPDATE_INTERVAL as A01_UPDATE_INTERVAL, DOMAIN as DOMAIN, IMAGE_CACHE_INTERVAL as IMAGE_CACHE_INTERVAL, V1_CLOUD_IN_CLEANING_INTERVAL as V1_CLOUD_IN_CLEANING_INTERVAL, V1_CLOUD_NOT_CLEANING_INTERVAL as V1_CLOUD_NOT_CLEANING_INTERVAL, V1_LOCAL_IN_CLEANING_INTERVAL as V1_LOCAL_IN_CLEANING_INTERVAL, V1_LOCAL_NOT_CLEANING_INTERVAL as V1_LOCAL_NOT_CLEANING_INTERVAL
from .models import DeviceState as DeviceState
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import slugify as slugify
from propcache.api import cached_property
from roborock.data import HomeDataScene as HomeDataScene
from roborock.devices.device import RoborockDevice as RoborockDevice
from roborock.devices.traits.a01 import DyadApi as DyadApi, ZeoApi as ZeoApi
from roborock.devices.traits.v1 import PropertiesApi as PropertiesApi
from roborock.roborock_message import RoborockDyadDataProtocol, RoborockZeoProtocol
from typing import Any, TypeVar

SCAN_INTERVAL: Incomplete
MIN_UNAVAILABLE_DURATION: Incomplete
_LOGGER: Incomplete

@dataclass
class RoborockCoordinators:
    v1: list[RoborockDataUpdateCoordinator]
    a01: list[RoborockDataUpdateCoordinatorA01]
    def values(self) -> list[RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01]: ...
type RoborockConfigEntry = ConfigEntry[RoborockCoordinators]

class RoborockDataUpdateCoordinator(DataUpdateCoordinator[DeviceState]):
    config_entry: RoborockConfigEntry
    _device: Incomplete
    properties_api: Incomplete
    device_info: Incomplete
    last_update_state: str | None
    _last_home_update_attempt: datetime
    last_home_update: datetime | None
    _last_update_success_time: datetime | None
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, properties_api: PropertiesApi) -> None: ...
    @cached_property
    def dock_device_info(self) -> DeviceInfo: ...
    async def _async_setup(self) -> None: ...
    async def update_map(self) -> None: ...
    update_interval: Incomplete
    async def _verify_api(self) -> None: ...
    async def _update_device_prop(self) -> None: ...
    async def _async_update_data(self) -> DeviceState: ...
    def _should_suppress_update_failure(self) -> bool: ...
    async def get_routines(self) -> list[HomeDataScene]: ...
    async def execute_routines(self, routine_id: int) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
    @property
    def device(self) -> RoborockDevice: ...

async def _refresh_traits(traits: list[Any]) -> None: ...
_V = TypeVar('_V', bound=RoborockDyadDataProtocol | RoborockZeoProtocol)

class RoborockDataUpdateCoordinatorA01(DataUpdateCoordinator[dict[_V, StateType]]):
    config_entry: RoborockConfigEntry
    _device: Incomplete
    device_info: Incomplete
    request_protocols: list[_V]
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
    @property
    def device(self) -> RoborockDevice: ...

class RoborockWashingMachineUpdateCoordinator(RoborockDataUpdateCoordinatorA01[RoborockZeoProtocol]):
    api: Incomplete
    request_protocols: list[RoborockZeoProtocol]
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, api: ZeoApi) -> None: ...
    async def _async_update_data(self) -> dict[RoborockZeoProtocol, StateType]: ...

class RoborockWetDryVacUpdateCoordinator(RoborockDataUpdateCoordinatorA01[RoborockDyadDataProtocol]):
    api: Incomplete
    request_protocols: list[RoborockDyadDataProtocol]
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, api: DyadApi) -> None: ...
    async def _async_update_data(self) -> dict[RoborockDyadDataProtocol, StateType]: ...
