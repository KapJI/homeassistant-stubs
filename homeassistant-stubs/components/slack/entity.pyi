from .const import ATTR_URL as ATTR_URL, ATTR_USER_ID as ATTR_USER_ID, DATA_CLIENT as DATA_CLIENT, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from slack_sdk.web.async_client import AsyncWebClient as AsyncWebClient

class SlackEntity(Entity):
    _client: AsyncWebClient
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: dict[str, AsyncWebClient], description: EntityDescription, entry: ConfigEntry) -> None: ...
