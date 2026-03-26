from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item
from typing import Any

PARALLEL_UPDATES: int
COMPIT_GEAR_TO_HA: Incomplete
HA_STATE_TO_COMPIT: Incomplete
DEVICE_DEFINITIONS: dict[int, FanEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CompitFan(CoordinatorEntity[CompitDataUpdateCoordinator], FanEntity):
    _attr_speed_count: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    device_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, entity_description: FanEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def percentage(self) -> int | None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
