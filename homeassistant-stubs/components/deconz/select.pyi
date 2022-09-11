from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.select import DOMAIN as DOMAIN, SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor.presence import Presence

SENSITIVITY_TO_DECONZ: Incomplete
DECONZ_TO_SENSITIVITY: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzPresenceDeviceModeSelect(DeconzDevice[Presence], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE: Incomplete
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...

class DeconzPresenceSensitivitySelect(DeconzDevice[Presence], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE: Incomplete
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...

class DeconzPresenceTriggerDistanceSelect(DeconzDevice[Presence], SelectEntity):
    _name_suffix: str
    unique_id_suffix: str
    _update_key: str
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    TYPE: Incomplete
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...
