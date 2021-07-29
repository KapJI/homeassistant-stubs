from . import ShellyDeviceWrapper as ShellyDeviceWrapper
from .const import COAP as COAP, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN
from .entity import ShellyBlockEntity as ShellyBlockEntity
from .utils import async_remove_shelly_entity as async_remove_shelly_entity
from aioshelly import Block as Block
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RelaySwitch(ShellyBlockEntity, SwitchEntity):
    control_result: Any
    def __init__(self, wrapper: ShellyDeviceWrapper, block: Block) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_callback(self) -> None: ...
