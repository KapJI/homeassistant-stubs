from . import TailscaleEntity as TailscaleEntity
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tailscale import Device as TailscaleDevice

class TailscaleBinarySensorEntityDescriptionMixin:
    is_on_fn: Callable[[TailscaleDevice], Union[bool, None]]
    def __init__(self, is_on_fn) -> None: ...

class TailscaleBinarySensorEntityDescription(BinarySensorEntityDescription, TailscaleBinarySensorEntityDescriptionMixin):
    def __init__(self, is_on_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

BINARY_SENSORS: tuple[TailscaleBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailscaleBinarySensorEntity(TailscaleEntity, BinarySensorEntity):
    entity_description: TailscaleBinarySensorEntityDescription
    @property
    def is_on(self) -> Union[bool, None]: ...
