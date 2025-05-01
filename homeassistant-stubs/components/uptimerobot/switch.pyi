from .const import API_ATTR_OK as API_ATTR_OK, LOGGER as LOGGER
from .coordinator import UptimeRobotConfigEntry as UptimeRobotConfigEntry
from .entity import UptimeRobotEntity as UptimeRobotEntity
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UptimeRobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UptimeRobotSwitch(UptimeRobotEntity, SwitchEntity):
    _attr_translation_key: str
    @property
    def is_on(self) -> bool: ...
    async def _async_edit_monitor(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
