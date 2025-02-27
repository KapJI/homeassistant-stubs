from .const import ATTR_DURATION as ATTR_DURATION, ATTR_VOLUME as ATTR_VOLUME, DEFAULT_TRANSITION_DURATION as DEFAULT_TRANSITION_DURATION, DOMAIN as DOMAIN, SERVICE_TRANSITION_OFF as SERVICE_TRANSITION_OFF, SERVICE_TRANSITION_ON as SERVICE_TRANSITION_ON
from .models import SnoozConfigurationData as SnoozConfigurationData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.fan import ATTR_PERCENTAGE as ATTR_PERCENTAGE, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pysnooz.commands import SnoozCommandData as SnoozCommandData
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SnoozFan(FanEntity, RestoreEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_should_poll: bool
    _is_on: bool | None
    _percentage: int | None
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: SnoozConfigurationData) -> None: ...
    @callback
    def _async_write_state_changed(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_subscribe_to_device_change(self) -> Callable[[], None]: ...
    @property
    def percentage(self) -> int | None: ...
    @property
    def is_on(self) -> bool | None: ...
    @property
    def assumed_state(self) -> bool: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_transition_on(self, duration: int, **kwargs: Any) -> None: ...
    async def async_transition_off(self, duration: int, **kwargs: Any) -> None: ...
    async def _async_execute_command(self, command: SnoozCommandData) -> None: ...
