from .const import MANUFACTURER as MANUFACTURER
from .coordinator import QswDataCoordinator as QswDataCoordinator, QswFirmwareCoordinator as QswFirmwareCoordinator
from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class QswEntityType(StrEnum):
    LACP_PORT: Incomplete
    PORT: Incomplete

class QswDataEntity(CoordinatorEntity[QswDataCoordinator]):
    type_id: Incomplete
    product: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: QswDataCoordinator, entry: ConfigEntry, type_id: Union[int, None] = ...) -> None: ...
    def get_device_value(self, key: str, subkey: str, qsw_type: Union[QswEntityType, None] = ...) -> Any: ...

class QswEntityDescriptionMixin:
    subkey: str
    def __init__(self, subkey) -> None: ...

class QswEntityDescription(EntityDescription, QswEntityDescriptionMixin):
    attributes: Union[dict[str, list[str]], None]

class QswSensorEntity(QswDataEntity):
    entity_description: QswEntityDescription
    def _handle_coordinator_update(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    def _async_update_attrs(self) -> None: ...

class QswFirmwareEntity(CoordinatorEntity[QswFirmwareCoordinator]):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: QswFirmwareCoordinator, entry: ConfigEntry) -> None: ...
    def get_device_value(self, key: str, subkey: str) -> Any: ...
