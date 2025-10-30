from . import NASwebConfigEntry as NASwebConfigEntry
from .const import DOMAIN as DOMAIN, KEY_TEMP_SENSOR as KEY_TEMP_SENSOR, STATUS_UPDATE_MAX_TIME_INTERVAL as STATUS_UPDATE_MAX_TIME_INTERVAL
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import BaseCoordinatorEntity as BaseCoordinatorEntity, BaseDataUpdateCoordinatorProtocol as BaseDataUpdateCoordinatorProtocol
from webio_api import Input as NASwebInput, TempSensor as TempSensor

SENSOR_INPUT_TRANSLATION_KEY: str
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: NASwebConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class BaseSensorEntity(SensorEntity, BaseCoordinatorEntity):
    _attr_available: bool
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    def __init__(self, coordinator: BaseDataUpdateCoordinatorProtocol) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _set_attr_available(self, entity_last_update: float, available: bool | None) -> None: ...
    async def async_update(self) -> None: ...

class InputStateSensor(BaseSensorEntity):
    _attr_device_class: Incomplete
    _attr_options: list[str]
    _attr_translation_key = SENSOR_INPUT_TRANSLATION_KEY
    _input: Incomplete
    _attr_native_value: str | None
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BaseDataUpdateCoordinatorProtocol, nasweb_input: NASwebInput) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...

class TemperatureSensor(BaseSensorEntity):
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _temp_sensor: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BaseDataUpdateCoordinatorProtocol, nasweb_temp_sensor: TempSensor) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
