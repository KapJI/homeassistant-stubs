from .coordinator import WattwaechterConfigEntry as WattwaechterConfigEntry, WattwaechterCoordinator as WattwaechterCoordinator
from .entity import WattwaechterEntity as WattwaechterEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
KNOWN_OBIS_CODES: dict[str, SensorEntityDescription]
OBIS_PHASE: dict[str, str]

async def async_setup_entry(hass: HomeAssistant, entry: WattwaechterConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WattwaechterObisSensor(WattwaechterEntity, SensorEntity):
    entity_description: SensorEntityDescription
    _obis_code: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: WattwaechterCoordinator, description: SensorEntityDescription, obis_code: str) -> None: ...
    @property
    @override
    def native_value(self) -> float | str | None: ...
