from .const import CONF_COMMAND_TIMEOUT as CONF_COMMAND_TIMEOUT, LOGGER as LOGGER
from .utils import check_output_or_log as check_output_or_log
from _typeshed import Incomplete
from datetime import datetime, timedelta
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass
from homeassistant.components.sensor.helpers import async_parse_date_datetime as async_parse_date_datetime
from homeassistant.const import CONF_COMMAND as CONF_COMMAND, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE, ManualTriggerSensorEntity as ManualTriggerSensorEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_JSON_ATTRIBUTES: str
DEFAULT_NAME: str
TRIGGER_ENTITY_OPTIONS: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class CommandSensor(ManualTriggerSensorEntity):
    _attr_should_poll: bool
    data: Incomplete
    _attr_extra_state_attributes: Incomplete
    _json_attributes: Incomplete
    _attr_native_value: Incomplete
    _value_template: Incomplete
    _scan_interval: Incomplete
    _process_updates: Incomplete
    def __init__(self, data: CommandSensorData, config: ConfigType, value_template: Template | None, json_attributes: list[str] | None, scan_interval: timedelta) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
    async def _update_entity_state(self, now: datetime | None = None) -> None: ...
    async def _async_update(self) -> None: ...
    async def async_update(self) -> None: ...

class CommandSensorData:
    value: Incomplete
    hass: Incomplete
    command: Incomplete
    timeout: Incomplete
    def __init__(self, hass: HomeAssistant, command: str, command_timeout: int) -> None: ...
    def update(self) -> None: ...
