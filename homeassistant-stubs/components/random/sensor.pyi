from .const import DEFAULT_MAX as DEFAULT_MAX, DEFAULT_MIN as DEFAULT_MIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_MAXIMUM as CONF_MAXIMUM, CONF_MINIMUM as CONF_MINIMUM, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ATTR_MAXIMUM: str
ATTR_MINIMUM: str
DEFAULT_NAME: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RandomSensor(SensorEntity):
    _attr_translation_key: str
    _unrecorded_attributes: Incomplete
    _attr_name: Incomplete
    _minimum: Incomplete
    _maximum: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config: Mapping[str, Any], entry_id: str | None = None) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
