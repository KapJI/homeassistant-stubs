from .common import SynoApi as SynoApi
from .const import ATTRIBUTION as ATTRIBUTION, DOMAIN as DOMAIN
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class SynologyDSMRequiredKeysMixin:
    api_key: str
    def __init__(self, api_key) -> None: ...

class SynologyDSMEntityDescription(EntityDescription, SynologyDSMRequiredKeysMixin):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement) -> None: ...

class SynologyDSMBaseEntity(CoordinatorEntity[DataUpdateCoordinator[dict[str, dict[str, Any]]]]):
    entity_description: SynologyDSMEntityDescription
    unique_id: str
    _attr_attribution: Any
    _api: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class SynologyDSMDeviceEntity(SynologyDSMBaseEntity):
    _device_id: Any
    _device_name: Any
    _device_manufacturer: Any
    _device_model: Any
    _device_firmware: Any
    _device_type: Any
    _attr_name: Any
    _attr_device_info: Any
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, Any]]], description: SynologyDSMEntityDescription, device_id: Union[str, None] = ...) -> None: ...
