from .const import DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .schema import NotifySchema as NotifySchema
from _typeshed import Incomplete
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Notification as XknxNotification

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = ...) -> KNXNotificationService | None: ...

class KNXNotificationService(BaseNotificationService):
    devices: Incomplete
    def __init__(self, devices: list[XknxNotification]) -> None: ...
    @property
    def targets(self) -> dict[str, str]: ...
    async def async_send_message(self, message: str = ..., **kwargs: Any) -> None: ...
    async def _async_send_to_all_devices(self, message: str) -> None: ...
    async def _async_send_to_device(self, message: str, names: str) -> None: ...
