import asyncio
from . import OnkyoConfigEntry as OnkyoConfigEntry
from .const import DOMAIN as DOMAIN
from .receiver import ReceiverManager as ReceiverManager
from _typeshed import Incomplete
from aioonkyo import Status as Status, command
from enum import StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
POWER_ON_QUERY_DELAY: int

class Channel(StrEnum):
    FRONT_LEFT = 'front_left'
    FRONT_RIGHT = 'front_right'
    CENTER = 'center'
    SURROUND_LEFT = 'surround_left'
    SURROUND_RIGHT = 'surround_right'
    SURROUND_BACK_LEFT = 'surround_back_left'
    SURROUND_BACK_RIGHT = 'surround_back_right'
    SUBWOOFER = 'subwoofer'
    HEIGHT_1_LEFT = 'height_1_left'
    HEIGHT_1_RIGHT = 'height_1_right'
    HEIGHT_2_LEFT = 'height_2_left'
    HEIGHT_2_RIGHT = 'height_2_right'
    SUBWOOFER_2 = 'subwoofer_2'

ChannelMutingData: Incomplete
ChannelMutingDesired: Incomplete

class ChannelMutingCoordinator(DataUpdateCoordinator[ChannelMutingData]):
    config_entry: OnkyoConfigEntry
    manager: Incomplete
    data: Incomplete
    _desired: Incomplete
    _entities_added: bool
    _query_state_task: asyncio.Task[None] | None
    def __init__(self, hass: HomeAssistant, config_entry: OnkyoConfigEntry, manager: ReceiverManager) -> None: ...
    async def _connect_callback(self, _reconnect: bool) -> None: ...
    async def _disconnect_callback(self) -> None: ...
    def _cancel_tasks(self) -> None: ...
    def _query_state(self, delay: float = 0) -> None: ...
    async def _async_update_data(self) -> ChannelMutingData: ...
    async def async_send_command(self, channel: Channel, param: command.ChannelMuting.Param) -> None: ...
    async def _update_callback(self, message: Status) -> None: ...
