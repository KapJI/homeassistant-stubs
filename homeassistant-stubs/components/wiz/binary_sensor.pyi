from .const import DOMAIN as DOMAIN, SIGNAL_WIZ_PIR as SIGNAL_WIZ_PIR
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

OCCUPANCY_UNIQUE_ID: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizOccupancyEntity(WizEntity, BinarySensorEntity):
    _attr_device_class: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    _attr_is_on: Any
    def _async_update_attrs(self) -> None: ...
