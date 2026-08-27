from .const import DOMAIN as DOMAIN
from .coordinator import LunatoneConfigEntry as LunatoneConfigEntry, LunatoneScanDataUpdateCoordinator as LunatoneScanDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: LunatoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LunatoneDALIScanStatus(CoordinatorEntity[LunatoneScanDataUpdateCoordinator], BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _config_entry_unique_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LunatoneScanDataUpdateCoordinator, config_entry_unique_id: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
