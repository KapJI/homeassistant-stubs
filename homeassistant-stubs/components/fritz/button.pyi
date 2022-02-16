from .common import AvmWrapper as AvmWrapper
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

_LOGGER: Any

class FritzButtonDescriptionMixin:
    press_action: Callable
    def __init__(self, press_action) -> None: ...

class FritzButtonDescription(ButtonEntityDescription, FritzButtonDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

BUTTONS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzButton(ButtonEntity):
    entity_description: FritzButtonDescription
    avm_wrapper: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, description: FritzButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
