from .const import CID as CID, DATA_KEY_API as DATA_KEY_API, DOMAIN as DOMAIN, ICON as ICON
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, STATE_IDLE as STATE_IDLE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from phone_modem import PhoneModem as PhoneModem

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ModemCalleridSensor(SensorEntity):
    _attr_icon = ICON
    _attr_should_poll: bool
    api: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, api: PhoneModem, name: str, server_unique_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_incoming_call(self, new_state: str) -> None: ...
