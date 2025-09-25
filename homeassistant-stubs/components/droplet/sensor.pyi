from .const import DOMAIN as DOMAIN, KEY_CURRENT_FLOW_RATE as KEY_CURRENT_FLOW_RATE, KEY_SERVER_CONNECTIVITY as KEY_SERVER_CONNECTIVITY, KEY_SIGNAL_QUALITY as KEY_SIGNAL_QUALITY, KEY_VOLUME as KEY_VOLUME
from .coordinator import DropletConfigEntry as DropletConfigEntry, DropletDataCoordinator as DropletDataCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pydroplet.droplet import Droplet as Droplet

ML_L_CONVERSION: int

@dataclass(kw_only=True, frozen=True)
class DropletSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Droplet], float | str | None]
    last_reset_fn: Callable[[Droplet], datetime | None] = ...

SENSORS: list[DropletSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: DropletConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DropletSensor(CoordinatorEntity[DropletDataCoordinator], SensorEntity):
    entity_description: DropletSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DropletDataCoordinator, entity_description: DropletSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | str | None: ...
    @property
    def last_reset(self) -> datetime | None: ...
