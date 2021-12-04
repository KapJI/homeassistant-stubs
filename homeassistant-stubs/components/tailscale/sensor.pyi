from . import TailscaleEntity as TailscaleEntity
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tailscale import Device as TailscaleDevice

class TailscaleSensorEntityDescriptionMixin:
    value_fn: Callable[[TailscaleDevice], Union[datetime, str, None]]

class TailscaleSensorEntityDescription(SensorEntityDescription, TailscaleSensorEntityDescriptionMixin): ...

SENSORS: tuple[TailscaleSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailscaleSensorEntity(TailscaleEntity, SensorEntity):
    entity_description: TailscaleSensorEntityDescription
    @property
    def native_value(self) -> Union[datetime, str, None]: ...
