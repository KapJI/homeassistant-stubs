from .coordinator import CertExpiryDataUpdateCoordinator as CertExpiryDataUpdateCoordinator
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

class CertExpiryEntity(CoordinatorEntity[CertExpiryDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any]: ...
