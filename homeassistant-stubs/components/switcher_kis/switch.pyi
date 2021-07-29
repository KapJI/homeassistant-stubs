from . import SwitcherDeviceWrapper as SwitcherDeviceWrapper
from .const import CONF_AUTO_OFF as CONF_AUTO_OFF, CONF_TIMER_MINUTES as CONF_TIMER_MINUTES, SERVICE_SET_AUTO_OFF_NAME as SERVICE_SET_AUTO_OFF_NAME, SERVICE_TURN_ON_WITH_TIMER_NAME as SERVICE_TURN_ON_WITH_TIMER_NAME, SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from aioswitcher.api import SwitcherBaseResponse as SwitcherBaseResponse
from datetime import timedelta
from homeassistant.components.switch import DEVICE_CLASS_OUTLET as DEVICE_CLASS_OUTLET, DEVICE_CLASS_SWITCH as DEVICE_CLASS_SWITCH, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry, entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Any
SERVICE_SET_AUTO_OFF_SCHEMA: Any
SERVICE_TURN_ON_WITH_TIMER_SCHEMA: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherBaseSwitchEntity(CoordinatorEntity, SwitchEntity):
    wrapper: Any
    control_result: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, wrapper: SwitcherDeviceWrapper) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def _async_call_api(self, api: str, *args: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: dict) -> None: ...
    async def async_turn_off(self, **kwargs: dict) -> None: ...
    async def async_set_auto_off_service(self, auto_off: timedelta) -> None: ...
    async def async_turn_on_with_timer_service(self, timer_minutes: int) -> None: ...

class SwitcherPowerPlugSwitchEntity(SwitcherBaseSwitchEntity):
    _attr_device_class: Any

class SwitcherWaterHeaterSwitchEntity(SwitcherBaseSwitchEntity):
    _attr_device_class: Any
    async def async_set_auto_off_service(self, auto_off: timedelta) -> None: ...
    control_result: bool
    async def async_turn_on_with_timer_service(self, timer_minutes: int) -> None: ...
