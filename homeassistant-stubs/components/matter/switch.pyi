from .entity import MatterEntity as MatterEntity, MatterEntityDescriptionBaseClass as MatterEntityDescriptionBaseClass
from .helpers import get_matter as get_matter
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.common.models import device_types
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterSwitch(MatterEntity, SwitchEntity):
    entity_description: MatterSwitchEntityDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _update_from_device(self) -> None: ...

class MatterSwitchEntityDescription(SwitchEntityDescription, MatterEntityDescriptionBaseClass):
    def __init__(self, entity_cls, subscribe_attributes, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

MatterSwitchEntityDescriptionFactory: Incomplete
DEVICE_ENTITY: dict[type[device_types.DeviceType], Union[MatterEntityDescriptionBaseClass, list[MatterEntityDescriptionBaseClass]]]
