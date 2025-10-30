from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from switchbot_api import Device as Device, Remote as Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

SENSOR_TYPE_TEMPERATURE: str
SENSOR_TYPE_HUMIDITY: str
SENSOR_TYPE_BATTERY: str
SENSOR_TYPE_CO2: str
SENSOR_TYPE_POWER: str
SENSOR_TYPE_VOLTAGE: str
SENSOR_TYPE_CURRENT: str
SENSOR_TYPE_POWER_CONSUMPTION: str
SENSOR_TYPE_USED_ELECTRICITY: str
SENSOR_TYPE_LIGHTLEVEL: str
RELAY_SWITCH_2PM_SENSOR_TYPE_POWER: str
RELAY_SWITCH_2PM_SENSOR_TYPE_VOLTAGE: str
RELAY_SWITCH_2PM_SENSOR_TYPE_CURRENT: str
RELAY_SWITCH_2PM_SENSOR_TYPE_ELECTRICITY: str

@dataclass(frozen=True, kw_only=True)
class SwitchbotCloudSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Any], Any] = ...

USED_ELECTRICITY_DESCRIPTION: Incomplete
TEMPERATURE_DESCRIPTION: Incomplete
HUMIDITY_DESCRIPTION: Incomplete
BATTERY_DESCRIPTION: Incomplete
POWER_DESCRIPTION: Incomplete
VOLTAGE_DESCRIPTION: Incomplete
CURRENT_DESCRIPTION_IN_MA: Incomplete
CURRENT_DESCRIPTION_IN_A: Incomplete
CO2_DESCRIPTION: Incomplete
POWER_CONSUMPTION_DESCRIPTION: Incomplete
RELAY_SWITCH_2PM_POWER_DESCRIPTION: Incomplete
RELAY_SWITCH_2PM_VOLTAGE_DESCRIPTION: Incomplete
RELAY_SWITCH_2PM_CURRENT_DESCRIPTION: Incomplete
RELAY_SWITCH_2PM_ElECTRICITY_DESCRIPTION: Incomplete
LIGHTLEVEL_DESCRIPTION: Incomplete
SENSOR_DESCRIPTIONS_BY_DEVICE_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SwitchBotCloudSensor(SwitchBotCloudEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device, coordinator: SwitchBotCoordinator, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _set_attributes(self) -> None: ...

class SwitchBotCloudRelaySwitch2PMSensor(SwitchBotCloudSensor):
    entity_description: Incomplete
    _channel: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device, coordinator: SwitchBotCoordinator, description: SensorEntityDescription, channel: str) -> None: ...
    _attr_native_value: Incomplete
    def _set_attributes(self) -> None: ...

@callback
def _async_make_entity(api: SwitchBotAPI, device: Device | Remote, coordinator: SwitchBotCoordinator, description: SensorEntityDescription) -> SwitchBotCloudSensor: ...
