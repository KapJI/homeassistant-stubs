from .. import mysensors as mysensors
from .const import ATTR_GATEWAY_ID as ATTR_GATEWAY_ID, ATTR_NODE_ID as ATTR_NODE_ID, DOMAIN as DOMAIN, DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY, MYSENSORS_GATEWAYS as MYSENSORS_GATEWAYS, MYSENSORS_NODE_DISCOVERY as MYSENSORS_NODE_DISCOVERY, NodeDiscoveryInfo as NodeDiscoveryInfo
from .helpers import on_unload as on_unload
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONDUCTIVITY as CONDUCTIVITY, DEGREE as DEGREE, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from mysensors import BaseAsyncGateway as BaseAsyncGateway
from typing import Any

SENSORS: dict[str, SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MyBatterySensor(mysensors.device.MySensorNodeEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_force_update: bool
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    _attr_native_value: Incomplete
    def _async_update_callback(self) -> None: ...

class MySensorsSensor(mysensors.device.MySensorsChildEntity, SensorEntity):
    _attr_force_update: bool
    entity_description: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    def _get_entity_description(self) -> SensorEntityDescription | None: ...
