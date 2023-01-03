from .common import SynoApi as SynoApi
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class SynologyDSMRequiredKeysMixin:
    api_key: str
    def __init__(self, api_key) -> None: ...

class SynologyDSMEntityDescription(EntityDescription, SynologyDSMRequiredKeysMixin):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

class SynologyDSMBaseEntity(CoordinatorEntity[DataUpdateCoordinator[dict[str, dict[str, Any]]]]):
    entity_description: SynologyDSMEntityDescription
    unique_id: str
    _attr_attribution: Incomplete
    _api: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class SynologyDSMDeviceEntity(SynologyDSMBaseEntity):
    _device_id: Incomplete
    _device_name: Incomplete
    _device_manufacturer: Incomplete
    _device_model: Incomplete
    _device_firmware: Incomplete
    _device_type: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMEntityDescription, device_id: Union[str, None] = ...) -> None: ...
