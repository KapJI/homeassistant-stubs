from . import OmadaConfigEntry as OmadaConfigEntry
from .const import OmadaDeviceStatus as OmadaDeviceStatus
from .coordinator import OmadaDevicesCoordinator as OmadaDevicesCoordinator
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice

DEVICE_STATUS_MAP: Incomplete
DEVICE_STATUS_CATEGORY_MAP: Incomplete

def _map_device_status(device: OmadaListDevice) -> str | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class OmadaDeviceSensorEntityDescription(SensorEntityDescription):
    exists_func: Callable[[OmadaListDevice], bool] = ...
    update_func: Callable[[OmadaListDevice], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., exists_func=..., update_func) -> None: ...

OMADA_DEVICE_SENSORS: list[OmadaDeviceSensorEntityDescription]

class OmadaDeviceSensor(OmadaDeviceEntity[OmadaDevicesCoordinator], SensorEntity):
    entity_description: OmadaDeviceSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OmadaDevicesCoordinator, device: OmadaListDevice, entity_description: OmadaDeviceSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
