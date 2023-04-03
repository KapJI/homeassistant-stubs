from .const import DOMAIN as DOMAIN
from .entity import VelbusEntity as VelbusEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from velbusaio.channels import Button as VelbusaioButton, ButtonCounter as VelbusaioButtonCounter

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusButton(VelbusEntity, ButtonEntity):
    _channel: VelbusaioButton | VelbusaioButtonCounter
    _attr_entity_registry_enabled_default: bool
    _attr_entity_category: Incomplete
    async def async_press(self) -> None: ...
