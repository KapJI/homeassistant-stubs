from .const import DOMAIN as DOMAIN
from .models import RoborockA01HassDeviceInfo as RoborockA01HassDeviceInfo, RoborockHassDeviceInfo as RoborockHassDeviceInfo, RoborockMapInfo as RoborockMapInfo
from .roborock_storage import RoborockMapStorage as RoborockMapStorage
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import slugify as slugify
from propcache.api import cached_property
from roborock import HomeDataRoom as HomeDataRoom
from roborock.containers import HomeDataDevice as HomeDataDevice, HomeDataProduct as HomeDataProduct, HomeDataScene as HomeDataScene, NetworkInfo as NetworkInfo, UserData as UserData
from roborock.roborock_message import RoborockDyadDataProtocol, RoborockZeoProtocol
from roborock.roborock_typing import DeviceProp
from roborock.version_1_apis.roborock_local_client_v1 import RoborockLocalClientV1
from roborock.version_1_apis.roborock_mqtt_client_v1 import RoborockMqttClientV1 as RoborockMqttClientV1
from roborock.version_a01_apis import RoborockClientA01 as RoborockClientA01
from roborock.web_api import RoborockApiClient as RoborockApiClient

SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

@dataclass
class RoborockCoordinators:
    v1: list[RoborockDataUpdateCoordinator]
    a01: list[RoborockDataUpdateCoordinatorA01]
    def values(self) -> list[RoborockDataUpdateCoordinator | RoborockDataUpdateCoordinatorA01]: ...
type RoborockConfigEntry = ConfigEntry[RoborockCoordinators]

class RoborockDataUpdateCoordinator(DataUpdateCoordinator[DeviceProp]):
    config_entry: RoborockConfigEntry
    roborock_device_info: Incomplete
    api: RoborockLocalClientV1 | RoborockMqttClientV1
    cloud_api: Incomplete
    device_info: Incomplete
    current_map: int | None
    maps: dict[int, RoborockMapInfo]
    _home_data_rooms: Incomplete
    map_storage: Incomplete
    _user_data: Incomplete
    _api_client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: HomeDataDevice, device_networking: NetworkInfo, product_info: HomeDataProduct, cloud_api: RoborockMqttClientV1, home_data_rooms: list[HomeDataRoom], api_client: RoborockApiClient, user_data: UserData) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _verify_api(self) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def _update_device_prop(self) -> None: ...
    async def _async_update_data(self) -> DeviceProp: ...
    def _set_current_map(self) -> None: ...
    async def set_current_map_rooms(self) -> None: ...
    async def get_scenes(self) -> list[HomeDataScene]: ...
    async def execute_scene(self, scene_id: int) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...

class RoborockDataUpdateCoordinatorA01(DataUpdateCoordinator[dict[RoborockDyadDataProtocol | RoborockZeoProtocol, StateType]]):
    config_entry: RoborockConfigEntry
    api: Incomplete
    device_info: Incomplete
    request_protocols: list[RoborockDyadDataProtocol | RoborockZeoProtocol]
    roborock_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RoborockConfigEntry, device: HomeDataDevice, product_info: HomeDataProduct, api: RoborockClientA01) -> None: ...
    async def _async_update_data(self) -> dict[RoborockDyadDataProtocol | RoborockZeoProtocol, StateType]: ...
    async def async_shutdown(self) -> None: ...
    @cached_property
    def duid(self) -> str: ...
    @cached_property
    def duid_slug(self) -> str: ...
