from .const import A01_UPDATE_INTERVAL as A01_UPDATE_INTERVAL, DOMAIN as DOMAIN, IMAGE_CACHE_INTERVAL as IMAGE_CACHE_INTERVAL, Q10_UPDATE_INTERVAL as Q10_UPDATE_INTERVAL, V1_CLOUD_IN_CLEANING_INTERVAL as V1_CLOUD_IN_CLEANING_INTERVAL, V1_CLOUD_NOT_CLEANING_INTERVAL as V1_CLOUD_NOT_CLEANING_INTERVAL, V1_LOCAL_IN_CLEANING_INTERVAL as V1_LOCAL_IN_CLEANING_INTERVAL, V1_LOCAL_NOT_CLEANING_INTERVAL as V1_LOCAL_NOT_CLEANING_INTERVAL
from .models import DeviceState as DeviceState, get_device_info as get_device_info
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import slugify as slugify
from propcache.api import cached_property
from roborock import B01Props
from roborock.data import HomeDataScene as HomeDataScene
from roborock.devices.device import RoborockDevice as RoborockDevice
from roborock.devices.traits.a01 import DyadApi as DyadApi, ZeoApi as ZeoApi
from roborock.devices.traits.b01 import Q10PropertiesApi as Q10PropertiesApi, Q7PropertiesApi as Q7PropertiesApi
from roborock.devices.traits.v1 import PropertiesApi as PropertiesApi
from roborock.roborock_message import RoborockB01Props, RoborockDyadDataProtocol, RoborockZeoProtocol
from typing import Any, override

SCAN_INTERVAL: Incomplete
MIN_UNAVAILABLE_DURATION: Incomplete
_LOGGER: Incomplete

class RoborockCoordinators:
    _coordinators: dict[str, RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | RoborockB01Q7UpdateCoordinator | RoborockB01Q10UpdateCoordinator]
    def __init__(self) -> None: ...
    def add(self, coordinator: RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | RoborockB01Q7UpdateCoordinator | RoborockB01Q10UpdateCoordinator) -> None: ...
    def __contains__(self, duid: str) -> bool: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01 | RoborockB01Q7UpdateCoordinator | RoborockB01Q10UpdateCoordinator]: ...
    @property
    def v1(self) -> list[RoborockDataUpdateCoordinator]: ...
    @property
    def a01(self) -> list[RoborockDataUpdateCoordinatorA01]: ...
    @property
    def b01_q7(self) -> list[RoborockB01Q7UpdateCoordinator]: ...
    @property
    def b01_q10(self) -> list[RoborockB01Q10UpdateCoordinator]: ...
type RoborockConfigEntry = ConfigEntry[RoborockCoordinators]

class RoborockDataUpdateCoordinator(DataUpdateCoordinator[DeviceState | None]):
    config_entry: RoborockConfigEntry
    _device: Incomplete
    properties_api: Incomplete
    device_info: Incomplete
    last_update_state: str | None
    _last_home_update_attempt: Incomplete
    last_home_update: datetime | None
    _last_update_success_time: datetime | None
    _has_connected_locally: bool
    _unsubs: list[Callable[[], None]]
    _setup_completed: bool
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, properties_api: PropertiesApi) -> None: ...
    @cached_property
    def dock_device_info(self) -> DeviceInfo: ...
    @override
    async def _async_setup(self) -> None: ...
    async def update_map(self) -> None: ...
    update_interval: Incomplete
    async def _verify_api(self) -> None: ...
    async def _update_device_prop(self) -> None: ...
    @override
    async def _async_update_data(self) -> DeviceState | None: ...
    def _should_suppress_update_failure(self) -> bool: ...
    @property
    def _device_state(self) -> DeviceState: ...
    @callback
    def _handle_trait_update(self) -> None: ...
    @override
    async def async_shutdown(self) -> None: ...
    async def get_routines(self) -> list[HomeDataScene]: ...
    async def execute_routines(self, routine_id: int) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
    @property
    def device(self) -> RoborockDevice: ...

async def _refresh_traits(traits: list[Any]) -> None: ...

class RoborockDataUpdateCoordinatorA01[_V: RoborockDyadDataProtocol | RoborockZeoProtocol](DataUpdateCoordinator[dict[_V, StateType]]):
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

ZEO_REQUEST_PROTOCOLS: Incomplete

class RoborockWashingMachineUpdateCoordinator(RoborockDataUpdateCoordinatorA01[RoborockZeoProtocol]):
    api: Incomplete
    request_protocols: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, api: ZeoApi) -> None: ...
    @override
    async def _async_update_data(self) -> dict[RoborockZeoProtocol, StateType]: ...

DYAD_REQUEST_PROTOCOLS: Incomplete

class RoborockWetDryVacUpdateCoordinator(RoborockDataUpdateCoordinatorA01[RoborockDyadDataProtocol]):
    api: Incomplete
    request_protocols: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, api: DyadApi) -> None: ...
    @override
    async def _async_update_data(self) -> dict[RoborockDyadDataProtocol, StateType]: ...

class RoborockDataUpdateCoordinatorB01(DataUpdateCoordinator[B01Props]):
    config_entry: RoborockConfigEntry
    _device: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
    @property
    def device(self) -> RoborockDevice: ...

class RoborockB01Q7UpdateCoordinator(RoborockDataUpdateCoordinatorB01):
    api: Incomplete
    request_protocols: list[RoborockB01Props]
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, api: Q7PropertiesApi) -> None: ...
    @override
    async def _async_update_data(self) -> B01Props: ...

class RoborockB01Q10UpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: RoborockConfigEntry
    _device: Incomplete
    api: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: RoborockDevice, api: Q10PropertiesApi) -> None: ...
    @override
    async def _async_update_data(self) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
    @property
    def device(self) -> RoborockDevice: ...
type RoborockCoordinatorType = RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01[Any] | RoborockB01Q7UpdateCoordinator | RoborockB01Q10UpdateCoordinator
