from . import ModemCallerIdConfigEntry as ModemCallerIdConfigEntry
from .const import CID as CID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import RestoreSensor as RestoreSensor
from homeassistant.const import STATE_IDLE as STATE_IDLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from phone_modem import PhoneModem as PhoneModem

async def async_setup_entry(hass: HomeAssistant, entry: ModemCallerIdConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ModemCalleridSensor(RestoreSensor):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_translation_key: str
    api: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: PhoneModem, server_unique_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_incoming_call(self, new_state: str) -> None: ...
