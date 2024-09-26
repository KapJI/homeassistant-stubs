from .const import API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, CONF_UID as CONF_UID, DOMAIN as DOMAIN
from .coordinator import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class GuardianEntity(CoordinatorEntity[GuardianDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    def __init__(self, coordinator: GuardianDataUpdateCoordinator, description: EntityDescription) -> None: ...

class PairedSensorEntity(GuardianEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: GuardianDataUpdateCoordinator, description: EntityDescription) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValveControllerEntityDescription(EntityDescription):
    api_category: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., api_category) -> None: ...

class ValveControllerEntity(GuardianEntity):
    _diagnostics_coordinator: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, GuardianDataUpdateCoordinator], description: ValveControllerEntityDescription) -> None: ...
