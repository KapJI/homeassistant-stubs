from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from compit_inext_api.consts import CompitParameter
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
NO_SENSOR: str
ON_STATES: Incomplete
DESCRIPTIONS: dict[CompitParameter, BinarySensorEntityDescription]

@dataclass(frozen=True, kw_only=True)
class CompitDeviceDescription:
    name: str
    parameters: dict[CompitParameter, BinarySensorEntityDescription]

DEVICE_DEFINITIONS: dict[int, CompitDeviceDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

class CompitBinarySensor(CoordinatorEntity[CompitDataUpdateCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    device_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    parameter_code: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, device_name: str, parameter_code: CompitParameter, entity_description: BinarySensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
