from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME as DEVICE_DEFAULT_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

FAKE_INSTALL_SLEEP_TIME: float

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _fake_install() -> None: ...

class DemoUpdate(UpdateEntity):
    _attr_should_poll: bool
    _attr_installed_version: Incomplete
    _attr_device_class: Incomplete
    _attr_latest_version: Incomplete
    _attr_name: Incomplete
    _attr_release_summary: Incomplete
    _attr_release_url: Incomplete
    _attr_title: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, unique_id: str, name: str, title: Union[str, None], installed_version: Union[str, None], latest_version: Union[str, None], release_summary: Union[str, None] = ..., release_url: Union[str, None] = ..., support_progress: bool = ..., support_install: bool = ..., support_release_notes: bool = ..., device_class: Union[UpdateDeviceClass, None] = ...) -> None: ...
    _attr_in_progress: Incomplete
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
    def release_notes(self) -> Union[str, None]: ...
