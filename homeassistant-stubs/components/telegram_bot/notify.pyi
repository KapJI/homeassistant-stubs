from . import TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import ATTR_TITLE as ATTR_TITLE, CONF_CHAT_ID as CONF_CHAT_ID
from .entity import TelegramBotEntity as TelegramBotEntity
from _typeshed import Incomplete
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: TelegramBotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TelegramBotNotifyEntity(TelegramBotEntity, NotifyEntity):
    _attr_supported_features: Incomplete
    chat_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: TelegramBotConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
