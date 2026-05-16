from .const import STATUSES_ON as STATUSES_ON
from .coordinator import UptimeRobotConfigEntry as UptimeRobotConfigEntry
from .entity import UptimeRobotEntity as UptimeRobotEntity
from .utils import new_device_listener as new_device_listener, uptimerobot_api_call as uptimerobot_api_call
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyuptimerobot import UptimeRobotMonitor as UptimeRobotMonitor
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UptimeRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UptimeRobotSwitch(UptimeRobotEntity, SwitchEntity):
    _attr_translation_key: str
    @property
    def is_on(self) -> bool: ...
    @uptimerobot_api_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @uptimerobot_api_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
