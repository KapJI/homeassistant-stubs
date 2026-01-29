from .const import NETATMO_CREATE_WEATHER_BINARY_SENSOR as NETATMO_CREATE_WEATHER_BINARY_SENSOR
from .data_handler import NetatmoDevice as NetatmoDevice
from .entity import NetatmoWeatherModuleEntity as NetatmoWeatherModuleEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class NetatmoBinarySensorEntityDescription(BinarySensorEntityDescription):
    name: str | None = ...
    netatmo_name: str

NETATMO_WEATHER_BINARY_SENSOR_DESCRIPTIONS: Final[list[NetatmoBinarySensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NetatmoWeatherBinarySensor(NetatmoWeatherModuleEntity, BinarySensorEntity):
    entity_description: NetatmoBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoBinarySensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_is_on: bool
    @callback
    def async_update_callback(self) -> None: ...
