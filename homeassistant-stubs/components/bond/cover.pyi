from .const import BPUP_SUBS as BPUP_SUBS, DOMAIN as DOMAIN, HUB as HUB
from .entity import BondEntity as BondEntity
from .utils import BondDevice as BondDevice, BondHub as BondHub
from bond_api import BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.cover import CoverEntity as CoverEntity, DEVICE_CLASS_SHADE as DEVICE_CLASS_SHADE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondCover(BondEntity, CoverEntity):
    _attr_device_class: Any
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions) -> None: ...
    _attr_is_closed: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
