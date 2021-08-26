from .const import DOMAIN as DOMAIN
from .renault_entities import RenaultBatteryDataEntity as RenaultBatteryDataEntity, RenaultDataEntity as RenaultDataEntity
from .renault_hub import RenaultHub as RenaultHub
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_BATTERY_CHARGING as DEVICE_CLASS_BATTERY_CHARGING, DEVICE_CLASS_PLUG as DEVICE_CLASS_PLUG
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultPluggedInSensor(RenaultBatteryDataEntity, BinarySensorEntity):
    _attr_device_class: Any
    @property
    def is_on(self) -> Union[bool, None]: ...

class RenaultChargingSensor(RenaultBatteryDataEntity, BinarySensorEntity):
    _attr_device_class: Any
    @property
    def is_on(self) -> Union[bool, None]: ...
