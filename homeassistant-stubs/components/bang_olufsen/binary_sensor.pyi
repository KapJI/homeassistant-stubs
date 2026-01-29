from . import BeoConfigEntry as BeoConfigEntry
from .const import CONNECTION_STATUS as CONNECTION_STATUS, DOMAIN as DOMAIN, WebsocketNotification as WebsocketNotification
from .entity import BeoEntity as BeoEntity
from .util import supports_battery as supports_battery
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from mozart_api.models import BatteryState as BatteryState

async def async_setup_entry(hass: HomeAssistant, config_entry: BeoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BeoBinarySensorBatteryCharging(BinarySensorEntity, BeoEntity):
    _attr_device_class: Incomplete
    _attr_is_on: bool
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: BeoConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _update_battery_charging(self, data: BatteryState) -> None: ...
