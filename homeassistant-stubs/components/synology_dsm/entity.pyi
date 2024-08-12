from .common import SynoApi as SynoApi
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from .coordinator import SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMUpdateCoordinator as SynologyDSMUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class SynologyDSMEntityDescription(EntityDescription):
    api_key: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., api_key) -> None: ...

class SynologyDSMBaseEntity(CoordinatorEntity[_CoordinatorT]):
    entity_description: SynologyDSMEntityDescription
    unique_id: str
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _api: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, coordinator: _CoordinatorT, description: SynologyDSMEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class SynologyDSMDeviceEntity(SynologyDSMBaseEntity[SynologyDSMCentralUpdateCoordinator]):
    _device_id: Incomplete
    _device_name: Incomplete
    _device_manufacturer: Incomplete
    _device_model: Incomplete
    _device_firmware: Incomplete
    _device_type: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator, description: SynologyDSMEntityDescription, device_id: str | None = None) -> None: ...
