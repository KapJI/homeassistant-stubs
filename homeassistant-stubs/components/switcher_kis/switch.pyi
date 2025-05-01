from .const import CONF_AUTO_OFF as CONF_AUTO_OFF, CONF_TIMER_MINUTES as CONF_TIMER_MINUTES, SERVICE_SET_AUTO_OFF_NAME as SERVICE_SET_AUTO_OFF_NAME, SERVICE_TURN_ON_WITH_TIMER_NAME as SERVICE_TURN_ON_WITH_TIMER_NAME, SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .coordinator import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .entity import SwitcherEntity as SwitcherEntity
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any

_LOGGER: Incomplete
API_CONTROL_DEVICE: str
API_SET_AUTO_SHUTDOWN: str
API_SET_CHILD_LOCK: str
SERVICE_SET_AUTO_OFF_SCHEMA: VolDictType
SERVICE_TURN_ON_WITH_TIMER_SCHEMA: VolDictType

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitcherBaseSwitchEntity(SwitcherEntity, SwitchEntity):
    _attr_name: Incomplete
    control_result: bool | None
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator) -> None: ...
    _attr_is_on: Incomplete
    def _update_data(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_auto_off_service(self, auto_off: timedelta) -> None: ...
    async def async_turn_on_with_timer_service(self, timer_minutes: int) -> None: ...

class SwitcherPowerPlugSwitchEntity(SwitcherBaseSwitchEntity):
    _attr_device_class: Incomplete

class SwitcherWaterHeaterSwitchEntity(SwitcherBaseSwitchEntity):
    _attr_device_class: Incomplete
    async def async_set_auto_off_service(self, auto_off: timedelta) -> None: ...
    _attr_is_on: bool
    async def async_turn_on_with_timer_service(self, timer_minutes: int) -> None: ...

class SwitcherShutterChildLockBaseSwitchEntity(SwitcherEntity, SwitchEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_icon: str
    _cover_id: int
    control_result: bool | None
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, cover_id: int) -> None: ...
    _attr_is_on: Incomplete
    def _update_data(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class SwitcherShutterChildLockSingleSwitchEntity(SwitcherShutterChildLockBaseSwitchEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, cover_id: int) -> None: ...

class SwitcherShutterChildLockMultiSwitchEntity(SwitcherShutterChildLockBaseSwitchEntity):
    _attr_translation_key: str
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, cover_id: int) -> None: ...
