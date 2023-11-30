from . import DeskData as DeskData, IdasenDeskCoordinator as IdasenDeskCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

_LOGGER: Incomplete

@dataclass
class IdasenDeskButtonDescriptionMixin:
    press_action: Callable[[IdasenDeskCoordinator], Callable[[], Coroutine[Any, Any, Any]]]
    def __init__(self, press_action) -> None: ...

@dataclass
class IdasenDeskButtonDescription(ButtonEntityDescription, IdasenDeskButtonDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IdasenDeskButton(ButtonEntity):
    entity_description: IdasenDeskButtonDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _address: Incomplete
    _coordinator: Incomplete
    def __init__(self, address: str, device_info: DeviceInfo, coordinator: IdasenDeskCoordinator, description: IdasenDeskButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
