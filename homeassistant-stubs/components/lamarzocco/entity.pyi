from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_MAC as CONF_MAC
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoEntityDescription(EntityDescription):
    available_fn: Callable[[LaMarzoccoUpdateCoordinator], bool] = ...
    supported_fn: Callable[[LaMarzoccoUpdateCoordinator], bool] = ...

class LaMarzoccoBaseEntity(CoordinatorEntity[LaMarzoccoUpdateCoordinator]):
    _attr_has_entity_name: bool
    _unavailable_when_machine_off: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, key: str) -> None: ...
    @property
    def available(self) -> bool: ...

class LaMarzoccoEntity(LaMarzoccoBaseEntity):
    entity_description: LaMarzoccoEntityDescription
    @property
    def available(self) -> bool: ...
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, entity_description: LaMarzoccoEntityDescription) -> None: ...
