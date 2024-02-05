from .const import API as API, DOMAIN as DOMAIN
from .entity import Tami4EdgeBaseEntity as Tami4EdgeBaseEntity
from Tami4EdgeAPI import Tami4EdgeAPI as Tami4EdgeAPI
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class Tami4EdgeButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Tami4EdgeAPI], None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, press_fn) -> None: ...

BUTTONS: tuple[Tami4EdgeButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Tami4EdgeButton(Tami4EdgeBaseEntity, ButtonEntity):
    entity_description: Tami4EdgeButtonEntityDescription
    def press(self) -> None: ...
