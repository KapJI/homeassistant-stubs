from .const import CONF_INDEX as CONF_INDEX, CONF_SELECT as CONF_SELECT, DOMAIN as DOMAIN
from .coordinator import ScrapeCoordinator as ScrapeCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.components.sensor.helpers import async_parse_date_datetime as async_parse_date_datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE, ManualTriggerEntity as ManualTriggerEntity, TEMPLATE_SENSOR_BASE_SCHEMA as TEMPLATE_SENSOR_BASE_SCHEMA
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ScrapeSensor(CoordinatorEntity[ScrapeCoordinator], ManualTriggerEntity, SensorEntity):
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _select: Incomplete
    _attr: Incomplete
    _index: Incomplete
    _value_template: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: ScrapeCoordinator, trigger_entity_config: ConfigType, unit_of_measurement: str | None, state_class: str | None, select: str, attr: str | None, index: int, value_template: Template | None, yaml: bool) -> None: ...
    def _extract_value(self) -> Any: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_update_from_rest_data(self) -> None: ...
    @property
    def available(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...
