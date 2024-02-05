from .base import AcmedaBase as AcmedaBase
from .const import ACMEDA_HUB_UPDATE as ACMEDA_HUB_UPDATE, DOMAIN as DOMAIN
from .helpers import async_add_acmeda_entities as async_add_acmeda_entities
from .hub import PulseHub as PulseHub
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AcmedaBattery(AcmedaBase, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    @property
    def native_value(self) -> float | int | None: ...
