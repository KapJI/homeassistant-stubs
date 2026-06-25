from .const import ATTRIBUTION as ATTRIBUTION, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .hub import HVVConfigEntry as HVVConfigEntry
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pygti.models import StationInformationResponse as StationInformationResponse
from typing import Any, override

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HVVConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HvvDepartureBinarySensor(CoordinatorEntity, BinarySensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    coordinator: Incomplete
    idx: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, Any]], idx: str, config_entry: HVVConfigEntry) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
