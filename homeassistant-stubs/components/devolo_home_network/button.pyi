from .const import DOMAIN as DOMAIN, IDENTIFY as IDENTIFY, PAIRING as PAIRING, RESTART as RESTART, START_WPS as START_WPS
from .entity import DevoloEntity as DevoloEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device import Device as Device
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass
class DevoloButtonRequiredKeysMixin:
    press_func: Callable[[Device], Awaitable[bool]]
    def __init__(self, press_func) -> None: ...

@dataclass
class DevoloButtonEntityDescription(ButtonEntityDescription, DevoloButtonRequiredKeysMixin):
    def __init__(self, press_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BUTTON_TYPES: dict[str, DevoloButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloButtonEntity(DevoloEntity, ButtonEntity):
    entity_description: DevoloButtonEntityDescription
    def __init__(self, entry: ConfigEntry, description: DevoloButtonEntityDescription, device: Device) -> None: ...
    async def async_press(self) -> None: ...
