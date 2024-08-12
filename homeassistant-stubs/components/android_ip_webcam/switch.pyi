from .const import DOMAIN as DOMAIN
from .coordinator import AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from .entity import AndroidIPCamBaseEntity as AndroidIPCamBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydroid_ipcam import PyDroidIPCam as PyDroidIPCam
from typing import Any

@dataclass(frozen=True, kw_only=True)
class AndroidIPWebcamSwitchEntityDescription(SwitchEntityDescription):
    on_func: Callable[[PyDroidIPCam], Coroutine[Any, Any, bool]]
    off_func: Callable[[PyDroidIPCam], Coroutine[Any, Any, bool]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., on_func, off_func) -> None: ...

SWITCH_TYPES: tuple[AndroidIPWebcamSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPWebcamSettingSwitch(AndroidIPCamBaseEntity, SwitchEntity):
    entity_description: AndroidIPWebcamSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator, description: AndroidIPWebcamSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
