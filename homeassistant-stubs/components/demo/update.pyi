from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

FAKE_INSTALL_SLEEP_TIME: float

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _fake_install() -> None: ...

class DemoUpdate(UpdateEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_installed_version: Incomplete
    _attr_device_class: Incomplete
    _attr_latest_version: Incomplete
    _attr_release_summary: Incomplete
    _attr_release_url: Incomplete
    _attr_title: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, unique_id: str, device_name: str, title: str | None, installed_version: str | None, latest_version: str | None, release_summary: str | None = ..., release_url: str | None = ..., support_progress: bool = ..., support_install: bool = ..., support_release_notes: bool = ..., device_class: UpdateDeviceClass | None = ...) -> None: ...
    _attr_in_progress: Incomplete
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    def release_notes(self) -> str | None: ...
