from . import KNXModule as KNXModule
from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxYamlEntity as KnxYamlEntity
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.notify import BaseNotificationService as BaseNotificationService, NotifyEntity as NotifyEntity, migrate_notify_issue as migrate_notify_issue
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Notification as XknxNotification

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> KNXNotificationService | None: ...

class KNXNotificationService(BaseNotificationService):
    devices: Incomplete
    def __init__(self, devices: list[XknxNotification]) -> None: ...
    @property
    def targets(self) -> dict[str, str]: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
    async def _async_send_to_all_devices(self, message: str) -> None: ...
    async def _async_send_to_device(self, message: str, names: str) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_notification_instance(xknx: XKNX, config: ConfigType) -> XknxNotification: ...

class KNXNotify(KnxYamlEntity, NotifyEntity):
    _device: XknxNotification
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
