from .const import DOMAIN as DOMAIN
from .entity import BAFEntity as BAFEntity
from .models import BAFData as BAFData
from _typeshed import Incomplete
from aiobafi6 import Device as Device
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class BAFSwitchDescriptionMixin:
    value_fn: Callable[[Device], bool | None]
    def __init__(self, value_fn) -> None: ...

class BAFSwitchDescription(SwitchEntityDescription, BAFSwitchDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BASE_SWITCHES: Incomplete
AUTO_COMFORT_SWITCHES: Incomplete
FAN_SWITCHES: Incomplete
LIGHT_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFSwitch(BAFEntity, SwitchEntity):
    entity_description: BAFSwitchDescription
    _attr_unique_id: Incomplete
    def __init__(self, device: Device, description: BAFSwitchDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
