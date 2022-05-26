from .const import MANUFACTURER as MANUFACTURER
from .coordinator import QswUpdateCoordinator as QswUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class QswEntity(CoordinatorEntity[QswUpdateCoordinator]):
    product: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: QswUpdateCoordinator, entry: ConfigEntry) -> None: ...
    def get_device_value(self, key: str, subkey: str) -> Any: ...

class QswEntityDescriptionMixin:
    subkey: str
    def __init__(self, subkey) -> None: ...

class QswEntityDescription(EntityDescription, QswEntityDescriptionMixin):
    attributes: Union[dict[str, list[str]], None]

class QswSensorEntity(QswEntity):
    entity_description: QswEntityDescription
    def _handle_coordinator_update(self) -> None: ...
    _attr_extra_state_attributes: Incomplete
    def _async_update_attrs(self) -> None: ...
