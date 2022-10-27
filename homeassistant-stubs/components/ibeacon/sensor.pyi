from .const import DOMAIN as DOMAIN, SIGNAL_IBEACON_DEVICE_NEW as SIGNAL_IBEACON_DEVICE_NEW
from .coordinator import IBeaconCoordinator as IBeaconCoordinator
from .entity import IBeaconEntity as IBeaconEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LENGTH_METERS as LENGTH_METERS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ibeacon_ble import iBeaconAdvertisement as iBeaconAdvertisement

class IBeaconRequiredKeysMixin:
    value_fn: Callable[[iBeaconAdvertisement], Union[str, int, None]]
    def __init__(self, value_fn) -> None: ...

class IBeaconSensorEntityDescription(SensorEntityDescription, IBeaconRequiredKeysMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IBeaconSensorEntity(IBeaconEntity, SensorEntity):
    entity_description: IBeaconSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IBeaconCoordinator, description: IBeaconSensorEntityDescription, identifier: str, device_unique_id: str, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    _attr_available: bool
    _ibeacon_advertisement: Incomplete
    def _async_seen(self, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    def _async_unavailable(self) -> None: ...
    @property
    def native_value(self) -> Union[str, int, None]: ...
