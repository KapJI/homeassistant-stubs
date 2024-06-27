from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from lmcloud.lm_machine import LaMarzoccoMachine as LaMarzoccoMachine

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoEntityDescription(EntityDescription):
    available_fn: Callable[[LaMarzoccoMachine], bool] = ...
    supported_fn: Callable[[LaMarzoccoUpdateCoordinator], bool] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, available_fn, supported_fn) -> None: ...

class LaMarzoccoBaseEntity(CoordinatorEntity[LaMarzoccoUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, key: str) -> None: ...

class LaMarzoccoEntity(LaMarzoccoBaseEntity):
    entity_description: LaMarzoccoEntityDescription
    @property
    def available(self) -> bool: ...
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, entity_description: LaMarzoccoEntityDescription) -> None: ...
