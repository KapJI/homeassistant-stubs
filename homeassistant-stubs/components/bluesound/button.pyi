from . import BluesoundConfigEntry as BluesoundConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import BluesoundCoordinator as BluesoundCoordinator
from .media_player import DEFAULT_PORT as DEFAULT_PORT
from .utils import format_unique_id as format_unique_id
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyblu import Player as Player

async def async_setup_entry(hass: HomeAssistant, config_entry: BluesoundConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(kw_only=True, frozen=True)
class BluesoundButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Player], Awaitable[None]]

async def clear_sleep_timer(player: Player) -> None: ...
async def set_sleep_timer(player: Player) -> None: ...

BUTTON_DESCRIPTIONS: Incomplete

class BluesoundButton(CoordinatorEntity[BluesoundCoordinator], ButtonEntity):
    _attr_has_entity_name: bool
    entity_description: BluesoundButtonEntityDescription
    _player: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BluesoundCoordinator, player: Player, port: int, description: BluesoundButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
