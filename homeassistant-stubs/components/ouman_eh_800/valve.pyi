from .const import OumanDevice as OumanDevice
from .coordinator import OumanEh800ConfigEntry as OumanEh800ConfigEntry
from .entity import OumanEh800Entity as OumanEh800Entity, OumanEh800EntityDescription as OumanEh800EntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ouman_eh_800_api import IntControlOumanEndpoint

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OumanEh800ValveEntityDescription(OumanEh800EntityDescription, ValveEntityDescription): ...

VALVE_DESCRIPTIONS: dict[IntControlOumanEndpoint, OumanEh800ValveEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OumanEh800ValveEntity(OumanEh800Entity, ValveEntity):
    entity_description: OumanEh800ValveEntityDescription
    _endpoint: IntControlOumanEndpoint
    _attr_reports_position: bool
    _attr_supported_features: Incomplete
    @property
    def current_valve_position(self) -> int: ...
    async def async_set_valve_position(self, position: int) -> None: ...
