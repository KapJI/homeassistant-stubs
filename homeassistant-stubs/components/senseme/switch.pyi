from .const import DOMAIN as DOMAIN
from .entity import SensemeEntity as SensemeEntity
from _typeshed import Incomplete
from aiosenseme import SensemeFan as SensemeFan
from aiosenseme.device import SensemeDevice as SensemeDevice
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class SenseMESwitchEntityDescriptionMixin:
    value_fn: Callable[[SensemeFan], bool]
    set_fn: Callable[[SensemeFan, bool], None]
    def __init__(self, value_fn, set_fn) -> None: ...

class SenseMESwitchEntityDescription(SwitchEntityDescription, SenseMESwitchEntityDescriptionMixin):
    def __init__(self, value_fn, set_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

def _set_sleep_mode(device: SensemeDevice, value: bool) -> None: ...
def _set_motion_fan_auto(device: SensemeDevice, value: bool) -> None: ...
def _set_motion_light_auto(device: SensemeDevice, value: bool) -> None: ...

FAN_SWITCHES: Incomplete
FAN_LIGHT_SWITCHES: Incomplete
LIGHT_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HASensemeSwitch(SensemeEntity, SwitchEntity):
    entity_description: SenseMESwitchEntityDescription
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: SensemeFan, description: SenseMESwitchEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
