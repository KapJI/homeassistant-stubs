import upcloud_api
from .const import DOMAIN as DOMAIN
from .coordinator import UpCloudConfigEntry as UpCloudConfigEntry, UpCloudDataUpdateCoordinator as UpCloudDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_USERNAME as CONF_USERNAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PROBLEM as STATE_PROBLEM
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

ATTR_CORE_NUMBER: str
ATTR_HOSTNAME: str
ATTR_MEMORY_AMOUNT: str
ATTR_TITLE: str
ATTR_UUID: str
ATTR_ZONE: str
DEFAULT_COMPONENT_NAME: str
STATE_MAP: Incomplete

class UpCloudServerEntity(CoordinatorEntity[UpCloudDataUpdateCoordinator]):
    config_entry: Incomplete
    uuid: Incomplete
    def __init__(self, config_entry: UpCloudConfigEntry, uuid: str) -> None: ...
    @property
    def _server(self) -> upcloud_api.Server: ...
    @property
    @override
    def unique_id(self) -> str: ...
    @property
    @override
    def name(self) -> str: ...
    @property
    @override
    def icon(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    @override
    def device_info(self) -> DeviceInfo: ...
