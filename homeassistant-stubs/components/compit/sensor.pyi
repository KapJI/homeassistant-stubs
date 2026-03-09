from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from compit_inext_api.consts import CompitParameter
from dataclasses import dataclass
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
NO_SENSOR: str
DESCRIPTIONS: dict[CompitParameter, SensorEntityDescription]

@dataclass(frozen=True, kw_only=True)
class CompitDeviceDescription:
    name: str
    parameters: dict[CompitParameter, SensorEntityDescription]

DEVICE_DEFINITIONS: dict[int, CompitDeviceDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

class CompitSensor(CoordinatorEntity[CompitDataUpdateCoordinator], SensorEntity):
    device_id: Incomplete
    entity_description: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    parameter_code: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, device_name: str, parameter_code: CompitParameter, entity_description: SensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | str | None: ...
