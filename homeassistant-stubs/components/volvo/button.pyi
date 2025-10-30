from .const import DOMAIN as DOMAIN
from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from .entity import VolvoBaseEntity as VolvoBaseEntity, VolvoEntityDescription as VolvoEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class VolvoButtonDescription(VolvoEntityDescription, ButtonEntityDescription):
    api_command: str
    required_command_key: str
    data: dict[str, int] | None = ...

_DESCRIPTIONS: tuple[VolvoButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VolvoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VolvoButton(VolvoBaseEntity, ButtonEntity):
    entity_description: VolvoButtonDescription
    async def async_press(self) -> None: ...
    def _raise(self, command: str, *, status: str = '', message: str = '', exception: Exception | None = None) -> None: ...
