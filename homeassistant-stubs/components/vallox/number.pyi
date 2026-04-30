from .coordinator import ValloxConfigEntry as ValloxConfigEntry, ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME, EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

class ValloxNumberEntity(ValloxEntity, NumberEntity):
    entity_description: ValloxNumberEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValloxNumberEntityDescription(NumberEntityDescription):
    metric_key: str

NUMBER_ENTITIES: tuple[ValloxNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ValloxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
