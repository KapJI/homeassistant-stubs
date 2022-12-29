from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType

class OverkizButtonDescription(ButtonEntityDescription):
    press_args: Union[OverkizStateType, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, press_args) -> None: ...

BUTTON_DESCRIPTIONS: list[OverkizButtonDescription]
SUPPORTED_COMMANDS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizButton(OverkizDescriptiveEntity, ButtonEntity):
    entity_description: OverkizButtonDescription
    async def async_press(self) -> None: ...
