from . import FroniusConfigEntry as FroniusConfigEntry
from .coordinator import FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator
from .entity import FroniusEntity as FroniusEntity, FroniusEntityDescription as FroniusEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True)
class FroniusBinarySensorEntityDescription(FroniusEntityDescription, BinarySensorEntityDescription): ...

POWER_FLOW_BINARY_SENSOR_DESCRIPTIONS: list[FroniusBinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: FroniusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PowerFlowBinarySensor(FroniusEntity, BinarySensorEntity):
    entity_description: FroniusBinarySensorEntityDescription
    _attr_is_on: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusPowerFlowUpdateCoordinator, description: FroniusBinarySensorEntityDescription, solar_net_id: str) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
