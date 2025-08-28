from . import TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import ATTR_TITLE as ATTR_TITLE, CONF_CHAT_ID as CONF_CHAT_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: TelegramBotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TelegramBotNotifyEntity(NotifyEntity):
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    name: Incomplete
    _attr_device_info: Incomplete
    _target: Incomplete
    _service: Incomplete
    def __init__(self, config_entry: TelegramBotConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
