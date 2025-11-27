from .const import DOMAIN as DOMAIN
from .coordinator import GoogleWeatherConfigEntry as GoogleWeatherConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class GoogleWeatherBaseEntity(Entity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: GoogleWeatherConfigEntry, subentry: ConfigSubentry, unique_id_suffix: str | None = None) -> None: ...
