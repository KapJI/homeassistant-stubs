from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from .entity import DiffuserEntity as DiffuserEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiffuserSwitch(SwitchEntity, DiffuserEntity):
    _attr_icon: str
    _attr_is_on: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
