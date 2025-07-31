import abc
from .const import CONF_VIN as CONF_VIN, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import VolvoBaseCoordinator as VolvoBaseCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from volvocarsapi.models import VolvoCarsApiBaseModel as VolvoCarsApiBaseModel

def get_unique_id(vin: str, key: str) -> str: ...
def value_to_translation_key(value: str) -> str: ...

@dataclass(frozen=True, kw_only=True)
class VolvoEntityDescription(EntityDescription):
    api_field: str

class VolvoEntity(CoordinatorEntity[VolvoBaseCoordinator], metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    entity_description: VolvoEntityDescription
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: VolvoBaseCoordinator, description: VolvoEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
    @abstractmethod
    def _update_state(self, api_field: VolvoCarsApiBaseModel | None) -> None: ...
