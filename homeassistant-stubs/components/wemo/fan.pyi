from .const import SERVICE_RESET_FILTER_LIFE as SERVICE_RESET_FILTER_LIFE, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY
from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import int_states_in_range as int_states_in_range, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from pywemo import FanMode, Humidifier as Humidifier
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int
ATTR_CURRENT_HUMIDITY: str
ATTR_TARGET_HUMIDITY: str
ATTR_FAN_MODE: str
ATTR_FILTER_LIFE: str
ATTR_FILTER_EXPIRED: str
ATTR_WATER_LEVEL: str
SPEED_RANGE: Incomplete
SET_HUMIDITY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WemoHumidifier(WemoBinaryStateEntity, FanEntity):
    _attr_supported_features: Incomplete
    wemo: Humidifier
    _last_fan_on_mode: FanMode
    def __init__(self, coordinator: DeviceCoordinator) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def percentage(self) -> int: ...
    @property
    def speed_count(self) -> int: ...
    def _handle_coordinator_update(self) -> None: ...
    def turn_on(self, percentage: int | None = ..., preset_mode: str | None = ..., **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def set_percentage(self, percentage: int) -> None: ...
    def _set_percentage(self, percentage: int | None) -> None: ...
    def set_humidity(self, target_humidity: float) -> None: ...
    def reset_filter_life(self) -> None: ...
