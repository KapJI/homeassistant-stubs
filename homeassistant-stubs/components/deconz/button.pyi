from .deconz_device import DeconzDevice as DeconzDevice, DeconzSceneMixin as DeconzSceneMixin
from .hub import DeconzHub as DeconzHub
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.scene import Scene as PydeconzScene
from pydeconz.models.sensor.presence import Presence

@dataclass(frozen=True, kw_only=True)
class DeconzButtonDescription(ButtonEntityDescription):
    button_fn: str
    suffix: str
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, button_fn, suffix) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzSceneButton(DeconzSceneMixin, ButtonEntity):
    TYPE = DOMAIN
    entity_description: Incomplete
    _attr_name: Incomplete
    def __init__(self, device: PydeconzScene, hub: DeconzHub, description: DeconzButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
    def get_device_identifier(self) -> str: ...

class DeconzPresenceResetButton(DeconzDevice[Presence], ButtonEntity):
    _name_suffix: str
    unique_id_suffix: str
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    TYPE = DOMAIN
    async def async_press(self) -> None: ...
