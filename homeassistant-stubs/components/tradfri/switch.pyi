from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID
from .coordinator import TradfriConfigEntry as TradfriConfigEntry, TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from .entity import TradfriBaseEntity as TradfriBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, config_entry: TradfriConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TradfriSwitch(TradfriBaseEntity, SwitchEntity):
    _attr_name: Incomplete
    _device_control: Incomplete
    _device_data: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Command | list[Command]], Any], gateway_id: str) -> None: ...
    @override
    def _refresh(self) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
