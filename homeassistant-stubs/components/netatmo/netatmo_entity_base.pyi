from .const import DATA_DEVICE_IDS as DATA_DEVICE_IDS, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODELS as MODELS, SIGNAL_NAME as SIGNAL_NAME
from .data_handler import NetatmoDataHandler as NetatmoDataHandler, PUBLICDATA_DATA_CLASS_NAME as PUBLICDATA_DATA_CLASS_NAME
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from typing import Any

class NetatmoBase(Entity):
    data_handler: Any
    _data_classes: Any
    _listeners: Any
    _device_name: str
    _id: str
    _model: str
    _attr_name: Any
    _attr_unique_id: Any
    _attr_extra_state_attributes: Any
    def __init__(self, data_handler: NetatmoDataHandler) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def async_update_callback(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
