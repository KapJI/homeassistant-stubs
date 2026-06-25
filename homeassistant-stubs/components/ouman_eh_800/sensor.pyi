from .const import OumanDevice as OumanDevice
from .coordinator import OumanEh800ConfigEntry as OumanEh800ConfigEntry
from .entity import OumanEh800Entity as OumanEh800Entity, OumanEh800EntityDescription as OumanEh800EntityDescription
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ouman_eh_800_api import OumanEndpoint as OumanEndpoint
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OumanEh800SensorDescription(OumanEh800EntityDescription, SensorEntityDescription): ...

def _temperature_sensor(*, device: OumanDevice, key: str, device_class: SensorDeviceClass = ..., entity_category: EntityCategory | None = None, enabled_by_default: bool = True) -> OumanEh800SensorDescription: ...
def _percentage_sensor(*, device: OumanDevice, key: str) -> OumanEh800SensorDescription: ...

SENSOR_DESCRIPTIONS: dict[OumanEndpoint, OumanEh800SensorDescription]

async def async_setup_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OumanEh800SensorEntity(OumanEh800Entity, SensorEntity):
    entity_description: OumanEh800SensorDescription
    @property
    @override
    def native_value(self) -> float | str: ...
