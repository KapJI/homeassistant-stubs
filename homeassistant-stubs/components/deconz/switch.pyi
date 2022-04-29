from .const import POWER_PLUGS as POWER_PLUGS
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.switch import DOMAIN as DOMAIN, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.light.light import Light as Light
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzPowerPlug(DeconzDevice, SwitchEntity):
    TYPE: Incomplete
    _device: Light
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
