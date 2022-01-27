from . import SynoApi as SynoApi
from .const import DOMAIN as DOMAIN, SYNO_API as SYNO_API
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

LOGGER: Any

class SynologyDSMbuttonDescriptionMixin:
    press_action: Callable[[SynoApi], Any]
    def __init__(self, press_action) -> None: ...

class SynologyDSMbuttonDescription(ButtonEntityDescription, SynologyDSMbuttonDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

BUTTONS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynologyDSMButton(ButtonEntity):
    entity_description: SynologyDSMbuttonDescription
    syno_api: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, api: SynoApi, description: SynologyDSMbuttonDescription) -> None: ...
    async def async_press(self) -> None: ...
