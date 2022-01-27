from . import RidwellEntity as RidwellEntity
from .const import DATA_ACCOUNT as DATA_ACCOUNT, DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN
from aioridwell.model import RidwellPickupEvent as RidwellPickupEvent
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SWITCH_TYPE_OPT_IN: str
SWITCH_DESCRIPTION: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RidwellSwitch(RidwellEntity, SwitchEntity):
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
