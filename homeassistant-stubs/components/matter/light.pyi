from .entity import MatterEntity as MatterEntity, MatterEntityDescriptionBaseClass as MatterEntityDescriptionBaseClass
from .helpers import get_matter as get_matter
from .util import renormalize as renormalize
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.common.models import device_types
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterLight(MatterEntity, LightEntity):
    entity_description: MatterLightEntityDescription
    def _supports_brightness(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_supported_color_modes: Incomplete
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    def _update_from_device(self) -> None: ...

class MatterLightEntityDescription(LightEntityDescription, MatterEntityDescriptionBaseClass):
    def __init__(self, entity_cls, subscribe_attributes, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

MatterLightEntityDescriptionFactory: Incomplete
DEVICE_ENTITY: dict[type[device_types.DeviceType], Union[MatterEntityDescriptionBaseClass, list[MatterEntityDescriptionBaseClass]]]
