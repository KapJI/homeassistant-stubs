from . import OmadaConfigEntry as OmadaConfigEntry
from .const import OmadaDeviceStatus as OmadaDeviceStatus
from .coordinator import OmadaDevicesCoordinator as OmadaDevicesCoordinator, OmadaSwitchPortCoordinator as OmadaSwitchPortCoordinator
from .entity import OmadaDeviceEntity as OmadaDeviceEntity, get_switch_port_base_name as get_switch_port_base_name
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice, OmadaSwitch as OmadaSwitch, OmadaSwitchPortDetails as OmadaSwitchPortDetails
from typing import override

PARALLEL_UPDATES: int
DEVICE_STATUS_MAP: Incomplete
DEVICE_STATUS_CATEGORY_MAP: Incomplete

def _map_device_status(device: OmadaListDevice) -> str | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class OmadaDeviceSensorEntityDescription(SensorEntityDescription):
    exists_func: Callable[[OmadaListDevice], bool] = ...
    update_func: Callable[[OmadaListDevice], StateType]

OMADA_DEVICE_SENSORS: list[OmadaDeviceSensorEntityDescription]

class OmadaDeviceSensor(OmadaDeviceEntity[OmadaDevicesCoordinator], SensorEntity):
    entity_description: OmadaDeviceSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OmadaDevicesCoordinator, device: OmadaListDevice, entity_description: OmadaDeviceSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...

@dataclass(frozen=True, kw_only=True)
class OmadaSwitchPortSensorEntityDescription(SensorEntityDescription):
    exists_func: Callable[[OmadaSwitch, OmadaSwitchPortDetails], bool] = ...
    update_func: Callable[[OmadaSwitchPortDetails], StateType]

OMADA_SWITCH_PORT_SENSORS: list[OmadaSwitchPortSensorEntityDescription]

class OmadaSwitchPortSensor(OmadaDeviceEntity[OmadaSwitchPortCoordinator], SensorEntity):
    entity_description: OmadaSwitchPortSensorEntityDescription
    _port_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: OmadaSwitchPortCoordinator, device: OmadaSwitch, port: OmadaSwitchPortDetails, entity_description: OmadaSwitchPortSensorEntityDescription, port_name: str) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
