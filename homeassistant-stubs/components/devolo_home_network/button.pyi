from . import DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from .const import DOMAIN as DOMAIN, IDENTIFY as IDENTIFY, PAIRING as PAIRING, RESTART as RESTART, START_WPS as START_WPS
from .entity import DevoloEntity as DevoloEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from devolo_plc_api.device import Device as Device
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class DevoloButtonEntityDescription(ButtonEntityDescription):
    press_func: Callable[[Device], Awaitable[bool]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, press_func) -> None: ...

BUTTON_TYPES: dict[str, DevoloButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloButtonEntity(DevoloEntity, ButtonEntity):
    entity_description: DevoloButtonEntityDescription
    def __init__(self, entry: DevoloHomeNetworkConfigEntry, description: DevoloButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
