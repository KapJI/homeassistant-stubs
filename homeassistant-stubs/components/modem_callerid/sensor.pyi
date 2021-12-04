from .const import CID as CID, DATA_KEY_API as DATA_KEY_API, DOMAIN as DOMAIN, ICON as ICON, SERVICE_REJECT_CALL as SERVICE_REJECT_CALL
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, STATE_IDLE as STATE_IDLE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from phone_modem import PhoneModem as PhoneModem
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: entity_platform.AddEntitiesCallback) -> None: ...

class ModemCalleridSensor(SensorEntity):
    _attr_icon: Any
    _attr_should_poll: bool
    device: Any
    api: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_value: Any
    _attr_extra_state_attributes: Any
    def __init__(self, api: PhoneModem, name: str, device: str, server_unique_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_incoming_call(self, new_state: str) -> None: ...
    async def async_reject_call(self) -> None: ...
