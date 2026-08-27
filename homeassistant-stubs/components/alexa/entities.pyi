from .capabilities import Alexa as Alexa, AlexaBrightnessController as AlexaBrightnessController, AlexaCameraStreamController as AlexaCameraStreamController, AlexaCapability as AlexaCapability, AlexaChannelController as AlexaChannelController, AlexaColorController as AlexaColorController, AlexaColorTemperatureController as AlexaColorTemperatureController, AlexaContactSensor as AlexaContactSensor, AlexaDoorbellEventSource as AlexaDoorbellEventSource, AlexaEndpointHealth as AlexaEndpointHealth, AlexaEqualizerController as AlexaEqualizerController, AlexaEventDetectionSensor as AlexaEventDetectionSensor, AlexaInputController as AlexaInputController, AlexaLockController as AlexaLockController, AlexaModeController as AlexaModeController, AlexaMotionSensor as AlexaMotionSensor, AlexaPlaybackController as AlexaPlaybackController, AlexaPlaybackStateReporter as AlexaPlaybackStateReporter, AlexaPowerController as AlexaPowerController, AlexaRangeController as AlexaRangeController, AlexaSceneController as AlexaSceneController, AlexaSecurityPanelController as AlexaSecurityPanelController, AlexaSeekController as AlexaSeekController, AlexaSpeaker as AlexaSpeaker, AlexaStepSpeaker as AlexaStepSpeaker, AlexaTemperatureSensor as AlexaTemperatureSensor, AlexaThermostatController as AlexaThermostatController, AlexaTimeHoldController as AlexaTimeHoldController, AlexaToggleController as AlexaToggleController
from .config import AbstractConfig as AbstractConfig
from .const import CONF_DISPLAY_CATEGORIES as CONF_DISPLAY_CATEGORIES
from _typeshed import Incomplete
from collections.abc import Generator, Iterable
from homeassistant.components import binary_sensor as binary_sensor, camera as camera, climate as climate, cover as cover, event as event, fan as fan, humidifier as humidifier, light as light, media_player as media_player, remote as remote, switch as switch, vacuum as vacuum, valve as valve, water_heater as water_heater
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntityStateAttribute as AlarmControlPanelEntityStateAttribute
from homeassistant.components.climate import ClimateEntityCapabilityAttribute as ClimateEntityCapabilityAttribute
from homeassistant.components.fan import FanEntityCapabilityAttribute as FanEntityCapabilityAttribute
from homeassistant.components.humidifier import HumidifierEntityCapabilityAttribute as HumidifierEntityCapabilityAttribute
from homeassistant.components.light import LightEntityCapabilityAttribute as LightEntityCapabilityAttribute
from homeassistant.components.media_player import MediaPlayerEntityCapabilityAttribute as MediaPlayerEntityCapabilityAttribute
from homeassistant.components.remote import RemoteEntityStateAttribute as RemoteEntityStateAttribute
from homeassistant.components.water_heater import WaterHeaterCapabilityAttribute as WaterHeaterCapabilityAttribute
from homeassistant.const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME, EntityStateAttribute as EntityStateAttribute, UnitOfTemperature as UnitOfTemperature, __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import intent as intent, network as network
from homeassistant.helpers.entity import entity_sources as entity_sources
from homeassistant.util.decorator import Registry as Registry
from typing import Any, override

_LOGGER: Incomplete
ENTITY_ADAPTERS: Registry[str, type[AlexaEntity]]
TRANSLATION_TABLE: Incomplete

class DisplayCategory:
    ACTIVITY_TRIGGER: str
    AIR_CONDITIONER: str
    AIR_FRESHENER: str
    AIR_PURIFIER: str
    AUTO_ACCESSORY: str
    CAMERA: str
    CHRISTMAS_TREE: str
    COFFEE_MAKER: str
    COMPUTER: str
    CONTACT_SENSOR: str
    DOOR: str
    DOORBELL: str
    EXTERIOR_BLIND: str
    FAN: str
    GAME_CONSOLE: str
    GARAGE_DOOR: str
    HEADPHONES: str
    HUB: str
    INTERIOR_BLIND: str
    LAPTOP: str
    LIGHT: str
    MICROWAVE: str
    MOBILE_PHONE: str
    MOTION_SENSOR: str
    MUSIC_SYSTEM: str
    NETWORK_HARDWARE: str
    OTHER: str
    OVEN: str
    PHONE: str
    PRINTER: str
    REMOTE: str
    ROUTER: str
    SCENE_TRIGGER: str
    SCREEN: str
    SECURITY_PANEL: str
    SECURITY_SYSTEM: str
    SLOW_COOKER: str
    SMARTLOCK: str
    SMARTPLUG: str
    SPEAKER: str
    STREAMING_DEVICE: str
    SWITCH: str
    TABLET: str
    TEMPERATURE_SENSOR: str
    THERMOSTAT: str
    TV: str
    VACUUM_CLEANER: str
    WATER_HEATER: str
    WEARABLE: str

class AlexaEntity:
    hass: Incomplete
    config: Incomplete
    entity: Incomplete
    entity_conf: Incomplete
    def __init__(self, hass: HomeAssistant, config: AbstractConfig, entity: State) -> None: ...
    @property
    def entity_id(self) -> str: ...
    def friendly_name(self) -> str: ...
    def description(self) -> str: ...
    def alexa_id(self) -> str: ...
    def display_categories(self) -> list[str] | None: ...
    def default_display_categories(self) -> list[str] | None: ...
    def interfaces(self) -> Iterable[AlexaCapability]: ...
    def serialize_properties(self) -> Generator[dict[str, Any]]: ...
    def serialize_discovery(self) -> dict[str, Any]: ...

@callback
def async_get_entities(hass: HomeAssistant, config: AbstractConfig) -> list[AlexaEntity]: ...

class GenericCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class SwitchCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class ButtonCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class ClimateCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class CoverCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class EventCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str] | None: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class LightCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class FanCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class RemoteCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class HumidifierCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class LockCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class MediaPlayerCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class SceneCapabilities(AlexaEntity):
    @override
    def description(self) -> str: ...
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class ScriptCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class SensorCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class BinarySensorCapabilities(AlexaEntity):
    TYPE_CONTACT: str
    TYPE_MOTION: str
    TYPE_PRESENCE: str
    @override
    def default_display_categories(self) -> list[str] | None: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...
    def get_type(self) -> str | None: ...

class AlarmControlPanelCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class ImageProcessingCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class InputNumberCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class TimerCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class VacuumCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class ValveCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...

class CameraCapabilities(AlexaEntity):
    @override
    def default_display_categories(self) -> list[str]: ...
    @override
    def interfaces(self) -> Generator[AlexaCapability]: ...
    def _check_requirements(self) -> bool: ...
