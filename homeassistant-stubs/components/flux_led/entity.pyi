import abc
from .const import CONF_MINOR_VERSION as CONF_MINOR_VERSION, CONF_MODEL as CONF_MODEL, DOMAIN as DOMAIN, SIGNAL_STATE_UPDATED as SIGNAL_STATE_UPDATED
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from abc import abstractmethod
from flux_led.aiodevice import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant import config_entries as config_entries
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

def _async_device_info(device: AIOWifiLedBulb, entry: config_entries.ConfigEntry) -> DeviceInfo: ...

class FluxBaseEntity(Entity):
    _attr_should_poll: bool
    _device: Any
    entry: Any
    _attr_device_info: Any
    def __init__(self, device: AIOWifiLedBulb, entry: config_entries.ConfigEntry) -> None: ...

class FluxEntity(CoordinatorEntity):
    coordinator: FluxLedUpdateCoordinator
    _device: Any
    _responding: bool
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: FluxLedUpdateCoordinator, base_unique_id: str, name: str, key: Union[str, None]) -> None: ...
    async def _async_ensure_device_on(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class FluxOnOffEntity(FluxEntity, metaclass=abc.ABCMeta):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @abstractmethod
    async def _async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
