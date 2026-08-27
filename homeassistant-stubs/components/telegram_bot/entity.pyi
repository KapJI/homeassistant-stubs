from . import TelegramBotConfigEntry as TelegramBotConfigEntry, bot_device_info as bot_device_info
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

class TelegramBotEntity(Entity):
    _attr_has_entity_name: bool
    _attr_device_info: DeviceInfo | None
    bot_id: Incomplete
    config_entry: Incomplete
    entity_description: Incomplete
    service: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: TelegramBotConfigEntry, entity_description: EntityDescription) -> None: ...
