from . import AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from abodepy.devices.cover import AbodeCover as AbodeCV
from homeassistant.components.cover import CoverEntity as CoverEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeCover(AbodeDevice, CoverEntity):
    _device: AbodeCV
    @property
    def is_closed(self) -> bool: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    def open_cover(self, **kwargs: Any) -> None: ...
