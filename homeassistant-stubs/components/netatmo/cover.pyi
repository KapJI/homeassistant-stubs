from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, NETATMO_CREATE_COVER as NETATMO_CREATE_COVER
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoCover(NetatmoBase, CoverEntity):
    _attr_supported_features: Incomplete
    _cover: Incomplete
    _id: Incomplete
    _attr_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _home_id: Incomplete
    _attr_is_closed: Incomplete
    _signal_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    @property
    def device_class(self) -> CoverDeviceClass: ...
    _attr_current_cover_position: Incomplete
    def async_update_callback(self) -> None: ...
