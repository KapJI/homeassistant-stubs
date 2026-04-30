from .const import DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, UFPConfigEntry as UFPConfigEntry
from .utils import async_ufp_instance_command as async_ufp_instance_command
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.siren import ATTR_DURATION as ATTR_DURATION, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any
from uiprotect.data import Siren as Siren

_LOGGER: Incomplete
PARALLEL_UPDATES: int
VALID_DURATIONS: tuple[int, ...]

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ProtectSiren(SirenEntity):
    _attr_has_entity_name: bool
    _attr_attribution = DEFAULT_ATTRIBUTION
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_supported_features: Incomplete
    data: Incomplete
    _siren_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _siren_mac: Incomplete
    _cancel_scheduled_off: CALLBACK_TYPE | None
    def __init__(self, data: ProtectData, siren: Siren) -> None: ...
    @property
    def _siren(self) -> Siren | None: ...
    _attr_available: Incomplete
    _attr_is_on: Incomplete
    @callback
    def _update_from_siren(self, siren: Siren) -> None: ...
    @callback
    def _async_updated(self, siren: Siren) -> None: ...
    @callback
    def _async_scheduled_off(self, _now: datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _cancel_off_timer(self) -> None: ...
    @async_ufp_instance_command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_ufp_instance_command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
