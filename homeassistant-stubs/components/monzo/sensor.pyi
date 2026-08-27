from .const import DEVICE_MODEL_ACCOUNT as DEVICE_MODEL_ACCOUNT, DEVICE_MODEL_POT as DEVICE_MODEL_POT, NON_TRANSFER_ACCOUNT_TYPES as NON_TRANSFER_ACCOUNT_TYPES
from .coordinator import MonzoConfigEntry as MonzoConfigEntry, MonzoCoordinator as MonzoCoordinator, MonzoData as MonzoData
from .entity import MonzoBaseEntity as MonzoBaseEntity
from .helpers import get_account_name as get_account_name
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MonzoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]

ACCOUNT_SENSORS: Incomplete
POT_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: MonzoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MonzoSensor(MonzoBaseEntity, SensorEntity):
    entity_description: MonzoSensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MonzoCoordinator, entity_description: MonzoSensorEntityDescription, resource_id: str, device_model: str, device_name: str, currency: str, data_accessor: Callable[[MonzoData], dict[str, dict[str, Any]]]) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
