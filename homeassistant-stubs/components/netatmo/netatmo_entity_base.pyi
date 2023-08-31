from .const import DATA_DEVICE_IDS as DATA_DEVICE_IDS, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DOMAIN as DOMAIN, SIGNAL_NAME as SIGNAL_NAME
from .data_handler import NetatmoDataHandler as NetatmoDataHandler, PUBLIC as PUBLIC
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class NetatmoBase(Entity):
    _attr_attribution = DEFAULT_ATTRIBUTION
    data_handler: Incomplete
    _publishers: Incomplete
    _device_name: str
    _id: str
    _model: str
    _config_url: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, data_handler: NetatmoDataHandler) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_update_callback(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
