from .const import DOMAIN as DOMAIN, DeviceResponseEntry as DeviceResponseEntry
from .coordinator import HWEnergyDeviceUpdateCoordinator as HWEnergyDeviceUpdateCoordinator
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

_LOGGER: Any
SENSORS: Final[tuple[SensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HWEnergySensor(CoordinatorEntity[DeviceResponseEntry], SensorEntity):
    entity_description: Any
    entry: Any
    _attr_name: Any
    data_type: Any
    _attr_unique_id: Any
    _attr_entity_registry_enabled_default: bool
    def __init__(self, coordinator: HWEnergyDeviceUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def data(self) -> DeviceResponseEntry: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
