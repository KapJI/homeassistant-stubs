from . import NtfyConfigEntry as NtfyConfigEntry
from .const import CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NtfyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NtfyNotifyEntity(NotifyEntity):
    entity_description: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    topic: Incomplete
    _attr_device_info: Incomplete
    config_entry: Incomplete
    ntfy: Incomplete
    def __init__(self, config_entry: NtfyConfigEntry, subentry: ConfigSubentry) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
