from .const import DOMAIN as DOMAIN
from .coordinator import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from .entity import AsekoEntity as AsekoEntity
from aioaseko import Unit as Unit
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AsekoBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Unit], bool | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., value_fn) -> None: ...

BINARY_SENSORS: tuple[AsekoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsekoBinarySensorEntity(AsekoEntity, BinarySensorEntity):
    entity_description: AsekoBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
