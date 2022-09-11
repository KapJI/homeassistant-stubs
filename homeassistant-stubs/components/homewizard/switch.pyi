from .const import DOMAIN as DOMAIN
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HWEnergySwitchEntity(CoordinatorEntity[HWEnergyDeviceUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, entry: ConfigEntry, key: str) -> None: ...

class HWEnergyMainSwitchEntity(HWEnergySwitchEntity):
    _attr_device_class: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, entry: ConfigEntry) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...

class HWEnergySwitchLockEntity(HWEnergySwitchEntity):
    _attr_name: str
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, entry: ConfigEntry) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
