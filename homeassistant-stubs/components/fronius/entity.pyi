from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase
from _typeshed import Incomplete
from collections.abc import Callable
from dataclasses import dataclass
from fronius_modbus import Controls, FroniusModbusInverter, Storage
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

type ModbusComponent = Controls | Storage
type ModbusComponentFn = Callable[[FroniusModbusInverter], ModbusComponent | None]
@dataclass(frozen=True)
class FroniusEntityDescription(EntityDescription):
    response_key: str | None = ...

class FroniusEntity(CoordinatorEntity['FroniusCoordinatorBase']):
    entity_description: FroniusEntityDescription
    _attr_has_entity_name: bool
    response_key: Incomplete
    solar_net_id: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: FroniusCoordinatorBase, description: FroniusEntityDescription, solar_net_id: str) -> None: ...
    def _device_data(self) -> dict[str, Any]: ...
