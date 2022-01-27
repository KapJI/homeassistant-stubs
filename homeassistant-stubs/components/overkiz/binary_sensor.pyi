from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

class OverkizBinarySensorDescriptionMixin:
    value_fn: Callable[[OverkizStateType], bool]
    def __init__(self, value_fn) -> None: ...

class OverkizBinarySensorDescription(BinarySensorEntityDescription, OverkizBinarySensorDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

BINARY_SENSOR_DESCRIPTIONS: list[OverkizBinarySensorDescription]
SUPPORTED_STATES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizBinarySensor(OverkizDescriptiveEntity, BinarySensorEntity):
    entity_description: OverkizBinarySensorDescription
    @property
    def is_on(self) -> Union[bool, None]: ...
