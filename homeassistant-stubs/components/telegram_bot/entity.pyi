from . import TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

class TelegramBotEntity(Entity):
    _attr_has_entity_name: bool
    bot_id: Incomplete
    config_entry: Incomplete
    entity_description: Incomplete
    service: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: TelegramBotConfigEntry, entity_description: EntityDescription) -> None: ...
