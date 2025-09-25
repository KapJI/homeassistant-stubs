from .const import DOMAIN as DOMAIN
from .coordinator import NtfyConfigEntry as NtfyConfigEntry
from .entity import NtfyBaseEntity as NtfyBaseEntity
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TITLE as ATTR_TITLE, NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
SERVICE_PUBLISH: str
ATTR_ATTACH: str
ATTR_CALL: str
ATTR_CLICK: str
ATTR_DELAY: str
ATTR_EMAIL: str
ATTR_ICON: str
ATTR_MARKDOWN: str
ATTR_PRIORITY: str
ATTR_TAGS: str
SERVICE_PUBLISH_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: NtfyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NtfyNotifyEntity(NtfyBaseEntity, NotifyEntity):
    entity_description: Incomplete
    _attr_supported_features: Incomplete
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
    async def publish(self, **kwargs: Any) -> None: ...
