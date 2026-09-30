from . import ThreemaConfigEntry as ThreemaConfigEntry
from .client import ThreemaAuthError as ThreemaAuthError, ThreemaConnectionError as ThreemaConnectionError, ThreemaSendError as ThreemaSendError
from .const import DOMAIN as DOMAIN, SUBENTRY_TYPE_RECIPIENT as SUBENTRY_TYPE_RECIPIENT
from _typeshed import Incomplete
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_RECIPIENT as CONF_RECIPIENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

async def async_setup_entry(hass: HomeAssistant, entry: ThreemaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ThreemaNotifyEntity(NotifyEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _client: Incomplete
    _recipient_id: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ThreemaConfigEntry, subentry: ConfigSubentry) -> None: ...
    @override
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
