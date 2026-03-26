from .coordinator import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .entity import JvcProjectorEntity as JvcProjectorEntity
from .util import deprecate_entity as deprecate_entity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from jvcprojector import Command as Command

@dataclass(frozen=True, kw_only=True)
class JvcProjectorSensorDescription(SensorEntityDescription):
    command: type[Command]

SENSORS: tuple[JvcProjectorSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class JvcProjectorSensorEntity(JvcProjectorEntity, SensorEntity):
    command: type[Command]
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _options_map: dict[str, str]
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator, description: JvcProjectorSensorDescription) -> None: ...
    @property
    def options(self) -> list[str] | None: ...
    @property
    def native_value(self) -> str | None: ...
