from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_SWITCH as NETATMO_CREATE_SWITCH
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoSwitch(NetatmoBase, SwitchEntity):
    _switch: Incomplete
    _id: Incomplete
    _attr_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _home_id: Incomplete
    _signal_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    def async_update_callback(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
