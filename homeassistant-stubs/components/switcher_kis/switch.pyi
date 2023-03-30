from . import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .const import CONF_AUTO_OFF as CONF_AUTO_OFF, CONF_TIMER_MINUTES as CONF_TIMER_MINUTES, SERVICE_SET_AUTO_OFF_NAME as SERVICE_SET_AUTO_OFF_NAME, SERVICE_TURN_ON_WITH_TIMER_NAME as SERVICE_TURN_ON_WITH_TIMER_NAME, SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from _typeshed import Incomplete
from aioswitcher.api import SwitcherBaseResponse as SwitcherBaseResponse
from datetime import timedelta
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
SERVICE_SET_AUTO_OFF_SCHEMA: Incomplete
SERVICE_TURN_ON_WITH_TIMER_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherBaseSwitchEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator], SwitchEntity):
    control_result: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def _async_call_api(self, api: str, *args: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_auto_off_service(self, auto_off: timedelta) -> None: ...
    async def async_turn_on_with_timer_service(self, timer_minutes: int) -> None: ...

class SwitcherPowerPlugSwitchEntity(SwitcherBaseSwitchEntity):
    _attr_device_class: Incomplete

class SwitcherWaterHeaterSwitchEntity(SwitcherBaseSwitchEntity):
    _attr_device_class: Incomplete
    async def async_set_auto_off_service(self, auto_off: timedelta) -> None: ...
    control_result: bool
    async def async_turn_on_with_timer_service(self, timer_minutes: int) -> None: ...
