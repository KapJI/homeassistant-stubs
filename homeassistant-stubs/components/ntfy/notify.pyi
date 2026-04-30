from .const import DOMAIN as DOMAIN
from .coordinator import NtfyConfigEntry as NtfyConfigEntry
from .entity import NtfyBaseEntity as NtfyBaseEntity
from .services import ACTIONS_MAP as ACTIONS_MAP, ATTR_ACTION as ATTR_ACTION, ATTR_ACTIONS as ATTR_ACTIONS, ATTR_ATTACH_FILE as ATTR_ATTACH_FILE, ATTR_FILENAME as ATTR_FILENAME, ATTR_SEQUENCE_ID as ATTR_SEQUENCE_ID
from _typeshed import Incomplete
from homeassistant.components import camera as camera, image as image
from homeassistant.components.media_source import async_resolve_media as async_resolve_media
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NtfyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NtfyNotifyEntity(NtfyBaseEntity, NotifyEntity):
    entity_description: Incomplete
    _attr_supported_features: Incomplete
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
    async def publish(self, **kwargs: Any) -> None: ...
    async def _publish(self, **kwargs: Any) -> None: ...
    async def clear(self, **kwargs: Any) -> None: ...
    async def delete(self, **kwargs: Any) -> None: ...
