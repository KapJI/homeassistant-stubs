from .const import DOMAIN as DOMAIN
from .entity import PowerWallEntity as PowerWallEntity
from .models import PowerwallRuntimeData as PowerwallRuntimeData
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerWallRunningSensor(PowerWallEntity, BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Any
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallConnectedSensor(PowerWallEntity, BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Any
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallGridServicesActiveSensor(PowerWallEntity, BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Any
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallGridStatusSensor(PowerWallEntity, BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Any
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...

class PowerWallChargingStatusSensor(PowerWallEntity, BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Any
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
