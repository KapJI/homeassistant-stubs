from . import IottyConfigEntry as IottyConfigEntry
from .api import IottyProxy as IottyProxy
from .coordinator import IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from .entity import IottyEntity as IottyEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from iottycloud.device import Device as Device
from iottycloud.lightswitch import LightSwitch
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: IottyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IottyLightSwitch(IottyEntity, SwitchEntity):
    _attr_device_class: Incomplete
    _iotty_device: LightSwitch
    def __init__(self, coordinator: IottyDataUpdateCoordinator, iotty_cloud: IottyProxy, iotty_device: LightSwitch) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
