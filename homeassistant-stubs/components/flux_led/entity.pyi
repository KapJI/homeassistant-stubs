import abc
from . import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .const import SIGNAL_STATE_UPDATED as SIGNAL_STATE_UPDATED
from abc import abstractmethod
from flux_led.aiodevice import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class FluxEntity(CoordinatorEntity):
    coordinator: FluxLedUpdateCoordinator
    _device: Any
    _responding: bool
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: FluxLedUpdateCoordinator, unique_id: Union[str, None], name: str) -> None: ...
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
