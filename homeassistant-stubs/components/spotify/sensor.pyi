from .coordinator import SpotifyConfigEntry as SpotifyConfigEntry, SpotifyCoordinator as SpotifyCoordinator
from .entity import SpotifyEntity as SpotifyEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from spotifyaio.models import AudioFeatures as AudioFeatures, Key

@dataclass(frozen=True, kw_only=True)
class SpotifyAudioFeaturesSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AudioFeatures], float | str | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

KEYS: dict[Key, str]
KEY_OPTIONS: Incomplete

def _get_key(audio_features: AudioFeatures) -> str | None: ...

AUDIO_FEATURE_SENSORS: tuple[SpotifyAudioFeaturesSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SpotifyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SpotifyAudioFeatureSensor(SpotifyEntity, SensorEntity):
    entity_description: SpotifyAudioFeaturesSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SpotifyCoordinator, entity_description: SpotifyAudioFeaturesSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | str | None: ...
