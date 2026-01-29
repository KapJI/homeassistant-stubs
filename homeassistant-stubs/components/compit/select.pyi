from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from compit_inext_api.consts import CompitParameter
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CompitDeviceDescription:
    name: str
    parameters: dict[CompitParameter, SelectEntityDescription]

DESCRIPTIONS: dict[CompitParameter, SelectEntityDescription]
DEVICE_DEFINITIONS: dict[int, CompitDeviceDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

class CompitSelect(CoordinatorEntity[CompitDataUpdateCoordinator], SelectEntity):
    device_id: Incomplete
    entity_description: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    parameter_code: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, device_name: str, parameter_code: CompitParameter, entity_description: SelectEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
