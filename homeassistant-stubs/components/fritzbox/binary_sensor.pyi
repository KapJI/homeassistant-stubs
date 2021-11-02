from . import FritzBoxEntity as FritzBoxEntity
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from .model import FritzEntityDescriptionMixinBase as FritzEntityDescriptionMixinBase
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_WINDOW as DEVICE_CLASS_WINDOW
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pyfritzhome.fritzhomedevice import FritzhomeDevice as FritzhomeDevice
from typing import Any, Final

class FritzEntityDescriptionMixinBinarySensor(FritzEntityDescriptionMixinBase):
    is_on: Callable[[FritzhomeDevice], Union[bool, None]]

class FritzBinarySensorEntityDescription(BinarySensorEntityDescription, FritzEntityDescriptionMixinBinarySensor): ...

BINARY_SENSOR_TYPES: Final[tuple[FritzBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxBinarySensor(FritzBoxEntity, BinarySensorEntity):
    entity_description: FritzBinarySensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, FritzhomeDevice]], ain: str, entity_description: FritzBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
