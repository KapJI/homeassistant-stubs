from .coordinator import HydrawiseConfigEntry as HydrawiseConfigEntry
from .entity import HydrawiseEntity as HydrawiseEntity
from _typeshed import Incomplete
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pydrawise.schema import Zone as Zone
from typing import Any

VALVE_TYPES: tuple[ValveEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: HydrawiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HydrawiseValve(HydrawiseEntity, ValveEntity):
    _attr_name: Incomplete
    _attr_reports_position: bool
    _attr_supported_features: Incomplete
    zone: Zone
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self) -> None: ...
    _attr_is_closed: Incomplete
    def _update_attrs(self) -> None: ...
