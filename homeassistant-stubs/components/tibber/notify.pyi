from . import DOMAIN as TIBBER_DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.notify import ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature, migrate_notify_issue as migrate_notify_issue
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from tibber import Tibber as Tibber
from typing import Any

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> TibberNotificationService: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TibberNotificationService(BaseNotificationService):
    _notify: Incomplete
    def __init__(self, notify: Callable) -> None: ...
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...

class TibberNotificationEntity(NotifyEntity):
    _attr_supported_features: Incomplete
    _attr_name = TIBBER_DOMAIN
    _attr_icon: str
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
