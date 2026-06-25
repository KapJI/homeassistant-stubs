from .coordinator import LaMetricConfigEntry as LaMetricConfigEntry, LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

async def async_setup_entry(hass: HomeAssistant, config_entry: LaMetricConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMetricUpdate(LaMetricEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator) -> None: ...
    @property
    @override
    def installed_version(self) -> str: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
