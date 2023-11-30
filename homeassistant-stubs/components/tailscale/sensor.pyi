from . import TailscaleEntity as TailscaleEntity
from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tailscale import Device as TailscaleDevice

@dataclass(kw_only=True)
class TailscaleSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TailscaleDevice], datetime | str | None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, *, value_fn) -> None: ...

SENSORS: tuple[TailscaleSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailscaleSensorEntity(TailscaleEntity, SensorEntity):
    entity_description: TailscaleSensorEntityDescription
    @property
    def native_value(self) -> datetime | str | None: ...
