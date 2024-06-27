from . import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud.models import LaMarzoccoMachineConfig as LaMarzoccoMachineConfig

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoBinarySensorEntityDescription(LaMarzoccoEntityDescription, BinarySensorEntityDescription):
    is_on_fn: Callable[[LaMarzoccoMachineConfig], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, available_fn, supported_fn, is_on_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoBinarySensorEntity(LaMarzoccoEntity, BinarySensorEntity):
    entity_description: LaMarzoccoBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
