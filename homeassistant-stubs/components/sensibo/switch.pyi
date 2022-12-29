from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, async_handle_api_call as async_handle_api_call
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysensibo.model import SensiboDevice as SensiboDevice
from typing import Any

PARALLEL_UPDATES: int

class DeviceBaseEntityDescriptionMixin:
    value_fn: Callable[[SensiboDevice], Union[bool, None]]
    extra_fn: Union[Callable[[SensiboDevice], dict[str, Union[str, bool, None]]], None]
    command_on: str
    command_off: str
    data_key: str
    def __init__(self, value_fn, extra_fn, command_on, command_off, data_key) -> None: ...

class SensiboDeviceSwitchEntityDescription(SwitchEntityDescription, DeviceBaseEntityDescriptionMixin):
    def __init__(self, value_fn, extra_fn, command_on, command_off, data_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

DEVICE_SWITCH_TYPES: tuple[SensiboDeviceSwitchEntityDescription, ...]
PURE_SWITCH_TYPES: tuple[SensiboDeviceSwitchEntityDescription, ...]
DESCRIPTION_BY_MODELS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboDeviceSwitch(SensiboDeviceBaseEntity, SwitchEntity):
    entity_description: SensiboDeviceSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    async def async_turn_on_timer(self, key: str, value: Any) -> bool: ...
    async def async_turn_off_timer(self, key: str, value: Any) -> bool: ...
    async def async_turn_on_off_pure_boost(self, key: str, value: Any) -> bool: ...
    async def async_turn_on_off_smart(self, key: str, value: Any) -> bool: ...
