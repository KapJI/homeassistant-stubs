from . import RpiPowerConfigEntry as RpiPowerConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, create_issue as create_issue
from rpi_bad_power import UnderVoltage as UnderVoltage

_LOGGER: Incomplete
DESCRIPTION_NORMALIZED: str
DESCRIPTION_UNDER_VOLTAGE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: RpiPowerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RaspberryChargerBinarySensor(BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _attr_has_entity_name: bool
    _attr_unique_id: str
    _under_voltage: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, under_voltage: UnderVoltage) -> None: ...
    _attr_is_on: Incomplete
    def update(self) -> None: ...
