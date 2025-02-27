from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBeeCoordinator as SwitchBeeCoordinator
from .entity import SwitchBeeDeviceEntity as SwitchBeeDeviceEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbee.device import SwitchBeeGroupSwitch, SwitchBeeSwitch, SwitchBeeTimedSwitch, SwitchBeeTimerSwitch
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBeeSwitchEntity[_DeviceTypeT: SwitchBeeTimedSwitch | SwitchBeeGroupSwitch | SwitchBeeSwitch | SwitchBeeTimerSwitch](SwitchBeeDeviceEntity[_DeviceTypeT], SwitchEntity):
    _attr_is_on: bool
    def __init__(self, device: _DeviceTypeT, coordinator: SwitchBeeCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    def _update_from_coordinator(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_state(self, state: str) -> None: ...
