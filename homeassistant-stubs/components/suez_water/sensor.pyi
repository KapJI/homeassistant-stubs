from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DOMAIN as DOMAIN
from .coordinator import SuezWaterCoordinator as SuezWaterCoordinator, SuezWaterData as SuezWaterData
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CURRENCY_EURO as CURRENCY_EURO, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pysuez.const import ATTRIBUTION
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SuezWaterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SuezWaterData], float | str | None]
    attr_fn: Callable[[SuezWaterData], Mapping[str, Any] | None] = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn, attr_fn=...) -> None: ...

SENSORS: tuple[SuezWaterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SuezWaterSensor(CoordinatorEntity[SuezWaterCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_attribution = ATTRIBUTION
    entity_description: SuezWaterSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SuezWaterCoordinator, counter_id: int, entity_description: SuezWaterSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | str | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
