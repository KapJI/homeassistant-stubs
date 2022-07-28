from .const import DOMAIN as DOMAIN
from .entity import LitterRobotEntity as LitterRobotEntity
from .hub import LitterRobotHub as LitterRobotHub
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

TYPE_RESET_WASTE_DRAWER: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LitterRobotResetWasteDrawerButton(LitterRobotEntity, ButtonEntity):
    _attr_icon: str
    _attr_entity_category: Incomplete
    async def async_press(self) -> None: ...
