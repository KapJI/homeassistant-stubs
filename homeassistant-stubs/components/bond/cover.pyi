from .const import BPUP_SUBS as BPUP_SUBS, DOMAIN as DOMAIN, HUB as HUB
from .entity import BondEntity as BondEntity
from .utils import BondDevice as BondDevice, BondHub as BondHub
from bond_api import BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.cover import CoverEntity as CoverEntity, DEVICE_CLASS_SHADE as DEVICE_CLASS_SHADE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, Callable

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: Callable[[list[Entity], bool], None]) -> None: ...

class BondCover(BondEntity, CoverEntity):
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions) -> None: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...