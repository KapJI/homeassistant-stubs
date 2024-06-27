from .const import CONF_CANDLE_LIGHT_MINUTES as CONF_CANDLE_LIGHT_MINUTES, CONF_DIASPORA as CONF_DIASPORA, CONF_HAVDALAH_OFFSET_MINUTES as CONF_HAVDALAH_OFFSET_MINUTES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LANGUAGE as CONF_LANGUAGE, CONF_LOCATION as CONF_LOCATION
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from typing import Any

class JewishCalendarEntity(Entity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _location: Incomplete
    _hebrew: Incomplete
    _candle_lighting_offset: Incomplete
    _havdalah_offset: Incomplete
    _diaspora: Incomplete
    def __init__(self, config_entry: ConfigEntry, data: dict[str, Any], description: EntityDescription) -> None: ...
