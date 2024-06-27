from .const import CONF_COUNTER_ID as CONF_COUNTER_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pysuez import SuezClient as SuezClient

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SuezSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    client: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, client: SuezClient, counter_id: int) -> None: ...
    _attr_native_value: Incomplete
    _attr_available: bool
    _attr_attribution: Incomplete
    def _fetch_data(self) -> None: ...
    def update(self) -> None: ...
