from .const import DEVICE_CLASS_CHARGE_MODE as DEVICE_CLASS_CHARGE_MODE, DEVICE_CLASS_CHARGE_STATE as DEVICE_CLASS_CHARGE_STATE, DEVICE_CLASS_PLUG_STATE as DEVICE_CLASS_PLUG_STATE, DOMAIN as DOMAIN
from .renault_entities import RenaultBatteryDataEntity as RenaultBatteryDataEntity, RenaultChargeModeDataEntity as RenaultChargeModeDataEntity, RenaultCockpitDataEntity as RenaultCockpitDataEntity, RenaultDataEntity as RenaultDataEntity, RenaultHVACDataEntity as RenaultHVACDataEntity
from .renault_hub import RenaultHub as RenaultHub
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, LENGTH_KILOMETERS as LENGTH_KILOMETERS, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT, TEMP_CELSIUS as TEMP_CELSIUS, TIME_MINUTES as TIME_MINUTES, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.util import slugify as slugify
from typing import Any

ATTR_BATTERY_AVAILABLE_ENERGY: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def get_entities(proxy: RenaultHub) -> list[RenaultDataEntity]: ...
async def get_vehicle_entities(vehicle: RenaultVehicleProxy) -> list[RenaultDataEntity]: ...

class RenaultBatteryAutonomySensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_icon: str
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...

class RenaultBatteryLevelSensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class RenaultBatteryTemperatureSensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...

class RenaultChargeModeSensor(RenaultChargeModeDataEntity, SensorEntity):
    _attr_device_class: Any
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def icon(self) -> str: ...

class RenaultChargeStateSensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_device_class: Any
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def icon(self) -> str: ...

class RenaultChargingRemainingTimeSensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_icon: str
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...

class RenaultChargingPowerSensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[float, None]: ...

class RenaultFuelAutonomySensor(RenaultCockpitDataEntity, SensorEntity):
    _attr_icon: str
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...

class RenaultFuelQuantitySensor(RenaultCockpitDataEntity, SensorEntity):
    _attr_icon: str
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...

class RenaultMileageSensor(RenaultCockpitDataEntity, SensorEntity):
    _attr_icon: str
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[int, None]: ...

class RenaultOutsideTemperatureSensor(RenaultHVACDataEntity, SensorEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    @property
    def state(self) -> Union[float, None]: ...

class RenaultPlugStateSensor(RenaultBatteryDataEntity, SensorEntity):
    _attr_device_class: Any
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def icon(self) -> str: ...
