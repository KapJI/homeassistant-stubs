from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tibber import Tibber as Tibber

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TibberNotificationEntity(NotifyEntity):
    _attr_supported_features: Incomplete
    _attr_name = DOMAIN
    _attr_icon: str
    _attr_unique_id: Incomplete
    def __init__(self, unique_id: str) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
