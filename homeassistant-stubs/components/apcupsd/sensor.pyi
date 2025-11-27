from .const import AVAILABLE_VIA_DEVICE_ATTR as AVAILABLE_VIA_DEVICE_ATTR, DEPRECATED_SENSORS as DEPRECATED_SENSORS, DOMAIN as DOMAIN, LAST_S_TEST as LAST_S_TEST
from .coordinator import APCUPSdConfigEntry as APCUPSdConfigEntry, APCUPSdCoordinator as APCUPSdCoordinator
from .entity import APCUPSdEntity as APCUPSdEntity
from _typeshed import Incomplete
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
_LOGGER: Incomplete
SENSORS: dict[str, SensorEntityDescription]
INFERRED_UNITS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: APCUPSdConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def infer_unit(value: str) -> tuple[str, str | None]: ...

class APCUPSdSensor(APCUPSdEntity, SensorEntity):
    def __init__(self, coordinator: APCUPSdCoordinator, description: SensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def _update_attrs(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
