from .const import DOMAIN as DOMAIN
from .coordinator import PurpleAirConfigEntry as PurpleAirConfigEntry, PurpleAirDataUpdateCoordinator as PurpleAirDataUpdateCoordinator
from _typeshed import Incomplete
from aiopurpleair.models.sensors import SensorModel as SensorModel
from collections.abc import Mapping
from homeassistant.const import CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, EntityStateAttribute as EntityStateAttribute
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

class PurpleAirEntity(CoordinatorEntity[PurpleAirDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _sensor_index: Incomplete
    _attr_device_info: Incomplete
    _entry: Incomplete
    def __init__(self, entry: PurpleAirConfigEntry, sensor_index: int) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def sensor_data(self) -> SensorModel: ...
