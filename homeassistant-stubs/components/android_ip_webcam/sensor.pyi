from .const import DOMAIN as DOMAIN
from .coordinator import AndroidIPCamDataUpdateCoordinator as AndroidIPCamDataUpdateCoordinator
from .entity import AndroidIPCamBaseEntity as AndroidIPCamBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pydroid_ipcam import PyDroidIPCam as PyDroidIPCam

@dataclass(frozen=True, kw_only=True)
class AndroidIPWebcamSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PyDroidIPCam], StateType]
    unit_fn: Callable[[PyDroidIPCam], str | None] = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn, unit_fn=...) -> None: ...

SENSOR_TYPES: tuple[AndroidIPWebcamSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPWebcamSensor(AndroidIPCamBaseEntity, SensorEntity):
    entity_description: AndroidIPWebcamSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AndroidIPCamDataUpdateCoordinator, description: AndroidIPWebcamSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
