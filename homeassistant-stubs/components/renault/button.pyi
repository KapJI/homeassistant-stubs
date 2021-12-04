from .const import DOMAIN as DOMAIN
from .renault_entities import RenaultEntity as RenaultEntity
from .renault_hub import RenaultHub as RenaultHub
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class RenaultButtonRequiredKeysMixin:
    async_press: Callable[[RenaultButtonEntity], Awaitable]

class RenaultButtonEntityDescription(ButtonEntityDescription, RenaultButtonRequiredKeysMixin):
    requires_electricity: bool

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultButtonEntity(RenaultEntity, ButtonEntity):
    entity_description: RenaultButtonEntityDescription
    async def async_press(self) -> None: ...

async def _start_charge(entity: RenaultButtonEntity) -> None: ...
async def _start_air_conditioner(entity: RenaultButtonEntity) -> None: ...

BUTTON_TYPES: tuple[RenaultButtonEntityDescription, ...]
