from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import NextDnsEntity as NextDnsEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
CLEAR_LOGS_BUTTON: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NextDnsButton(NextDnsEntity, ButtonEntity):
    async def async_press(self) -> None: ...
