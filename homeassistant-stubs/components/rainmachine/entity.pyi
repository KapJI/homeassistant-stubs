from . import RainMachineConfigEntry as RainMachineConfigEntry, RainMachineData as RainMachineData
from .const import DATA_API_VERSIONS as DATA_API_VERSIONS, DOMAIN as DOMAIN
from .coordinator import RainMachineDataUpdateCoordinator as RainMachineDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class RainMachineEntityDescription(EntityDescription):
    api_category: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., api_category) -> None: ...

class RainMachineEntity(CoordinatorEntity[RainMachineDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    _data: Incomplete
    _version_coordinator: Incomplete
    entity_description: Incomplete
    def __init__(self, entry: RainMachineConfigEntry, data: RainMachineData, description: RainMachineEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
