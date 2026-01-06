from .const import DOMAIN as DOMAIN, TibberConfigEntry as TibberConfigEntry
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: TibberConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TibberNotificationEntity(NotifyEntity):
    _attr_supported_features: Incomplete
    _attr_name = DOMAIN
    _attr_icon: str
    _attr_unique_id: Incomplete
    _entry: Incomplete
    def __init__(self, entry: TibberConfigEntry) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...
