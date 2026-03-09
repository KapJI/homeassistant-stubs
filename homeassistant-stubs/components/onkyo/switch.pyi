from . import OnkyoConfigEntry as OnkyoConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import Channel as Channel, ChannelMutingCoordinator as ChannelMutingCoordinator
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OnkyoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OnkyoChannelMutingSwitch(CoordinatorEntity[ChannelMutingCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    _channel: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ChannelMutingCoordinator, channel: Channel) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _handle_coordinator_update(self) -> None: ...
