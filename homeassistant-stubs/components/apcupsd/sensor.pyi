from . import APCUPSdData as APCUPSdData, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
SENSORS: dict[str, SensorEntityDescription]
SPECIFIC_UNITS: Incomplete
INFERRED_UNITS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def infer_unit(value: str) -> tuple[str, Union[str, None]]: ...

class APCUPSdSensor(SensorEntity):
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    _data_service: Incomplete
    def __init__(self, data_service: APCUPSdData, description: SensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def update(self) -> None: ...
