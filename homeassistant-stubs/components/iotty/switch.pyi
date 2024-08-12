from . import IottyConfigEntry as IottyConfigEntry
from .api import IottyProxy as IottyProxy
from .const import DOMAIN as DOMAIN
from .coordinator import IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from iottycloud.device import Device as Device
from iottycloud.lightswitch import LightSwitch
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: IottyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IottyLightSwitch(SwitchEntity, CoordinatorEntity[IottyDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_entity_category: Incomplete
    _attr_device_class: Incomplete
    _iotty_cloud: IottyProxy
    _iotty_device: LightSwitch
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IottyDataUpdateCoordinator, iotty_cloud: IottyProxy, iotty_device: LightSwitch) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
