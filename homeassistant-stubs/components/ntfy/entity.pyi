from .const import CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN
from .coordinator import NtfyConfigEntry as NtfyConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class NtfyBaseEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    topic: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    ntfy: Incomplete
    config_entry: Incomplete
    subentry: Incomplete
    def __init__(self, config_entry: NtfyConfigEntry, subentry: ConfigSubentry) -> None: ...
