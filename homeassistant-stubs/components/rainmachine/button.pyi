from . import RainMachineData as RainMachineData, RainMachineEntity as RainMachineEntity
from .const import DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DOMAIN as DOMAIN
from .model import RainMachineEntityDescription as RainMachineEntityDescription
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from regenmaschine.controller import Controller as Controller

@dataclass
class RainMachineButtonDescriptionMixin:
    push_action: Callable[[Controller], Awaitable]
    def __init__(self, push_action) -> None: ...

@dataclass
class RainMachineButtonDescription(ButtonEntityDescription, RainMachineEntityDescription, RainMachineButtonDescriptionMixin):
    def __init__(self, push_action, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BUTTON_KIND_REBOOT: str

async def _async_reboot(controller: Controller) -> None: ...

BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineButton(RainMachineEntity, ButtonEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    entity_description: RainMachineButtonDescription
    async def async_press(self) -> None: ...
