from .coordinator import UpCloudConfigEntry as UpCloudConfigEntry
from .entity import UpCloudServerEntity as UpCloudServerEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import STATE_OFF as STATE_OFF
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

SIGNAL_UPDATE_UPCLOUD: str

async def async_setup_entry(hass: HomeAssistant, config_entry: UpCloudConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UpCloudSwitch(UpCloudServerEntity, SwitchEntity):
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
