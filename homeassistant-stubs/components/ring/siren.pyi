from . import RingData as RingData
from .const import DOMAIN as DOMAIN
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingEntity as RingEntity, exception_wrap as exception_wrap
from _typeshed import Incomplete
from homeassistant.components.siren import ATTR_TONE as ATTR_TONE, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import RingChime
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingChimeSiren(RingEntity[RingChime], SirenEntity):
    _attr_available_tones: Incomplete
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, device: RingChime, coordinator: RingDataCoordinator) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
