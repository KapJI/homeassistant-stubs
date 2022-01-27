from . import HomeAssistantElgatoData as HomeAssistantElgatoData
from .const import DOMAIN as DOMAIN
from .entity import ElgatoEntity as ElgatoEntity
from elgato import Elgato as Elgato, Info as Info
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoIdentifyButton(ElgatoEntity, ButtonEntity):
    entity_description: Any
    _attr_unique_id: Any
    def __init__(self, client: Elgato, info: Info, mac: Union[str, None]) -> None: ...
    async def async_press(self) -> None: ...
