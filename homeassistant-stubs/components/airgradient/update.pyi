from . import AirGradientConfigEntry as AirGradientConfigEntry, AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from functools import cached_property as cached_property
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AirGradientConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirGradientUpdate(AirGradientEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator) -> None: ...
    @cached_property
    def should_poll(self) -> bool: ...
    @property
    def installed_version(self) -> str: ...
    _attr_latest_version: Incomplete
    async def async_update(self) -> None: ...
