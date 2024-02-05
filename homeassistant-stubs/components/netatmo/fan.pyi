from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_FAN as NETATMO_CREATE_FAN
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoBaseEntity as NetatmoBaseEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

_LOGGER: Incomplete
DEFAULT_PERCENTAGE: Final[int]
PRESET_MAPPING: Incomplete
PRESETS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoFan(NetatmoBaseEntity, FanEntity):
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _fan: Incomplete
    _id: Incomplete
    _attr_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _home_id: Incomplete
    _signal_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    _attr_preset_mode: Incomplete
    def async_update_callback(self) -> None: ...
