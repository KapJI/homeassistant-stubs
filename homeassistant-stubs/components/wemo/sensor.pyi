from .entity import WemoEntity as WemoEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import convert as convert
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class InsightSensor(WemoEntity, SensorEntity):
    @property
    def name_suffix(self) -> str: ...
    @property
    def unique_id_suffix(self) -> str: ...
    @property
    def available(self) -> bool: ...

class InsightCurrentPower(InsightSensor):
    entity_description: Any
    @property
    def native_value(self) -> StateType: ...

class InsightTodayEnergy(InsightSensor):
    entity_description: Any
    @property
    def native_value(self) -> StateType: ...
