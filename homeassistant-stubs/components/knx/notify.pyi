from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity, build_yaml_unique_id as build_yaml_unique_id
from .knx_module import KNXModule as KNXModule
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_SEND as CONF_GA_SEND
from .storage.util import ConfigExtractor as ConfigExtractor
from homeassistant import config_entries as config_entries
from homeassistant.components.notify import NotifyEntity as NotifyEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override
from xknx.devices import Notification as XknxNotification

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxNotify(NotifyEntity):
    _device: XknxNotification
    @override
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...

class KnxYamlNotify(_KnxNotify, KnxYamlEntity):
    _device: XknxNotification
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiNotify(_KnxNotify, KnxUiEntity):
    _device: XknxNotification
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
