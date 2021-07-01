from .const import DiscoveryInfo as DiscoveryInfo
from .helpers import on_unload as on_unload
from homeassistant.components import mysensors as mysensors
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES as DEVICE_CLASSES, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_SOUND as DEVICE_CLASS_SOUND, DEVICE_CLASS_VIBRATION as DEVICE_CLASS_VIBRATION, DOMAIN as DOMAIN
from homeassistant.components.mysensors.const import MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MySensorsBinarySensor(mysensors.device.MySensorsEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
    @property
    def device_class(self) -> Union[str, None]: ...
