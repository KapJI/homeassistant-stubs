from . import SwitchbotCloudData as SwitchbotCloudData
from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from .entity import SwitchBotCloudEntity as SwitchBotCloudEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from switchbot_api import Device as Device, SwitchBotAPI as SwitchBotAPI

SENSOR_TYPE_TEMPERATURE: str
SENSOR_TYPE_HUMIDITY: str
SENSOR_TYPE_BATTERY: str
METER_PLUS_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitchBotCloudSensor(SwitchBotCloudEntity, SensorEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, api: SwitchBotAPI, device: Device, coordinator: SwitchBotCoordinator, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _handle_coordinator_update(self) -> None: ...
