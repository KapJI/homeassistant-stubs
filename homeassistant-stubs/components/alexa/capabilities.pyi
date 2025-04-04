from .const import API_TEMP_UNITS as API_TEMP_UNITS, API_THERMOSTAT_MODES as API_THERMOSTAT_MODES, API_THERMOSTAT_PRESETS as API_THERMOSTAT_PRESETS, DATE_FORMAT as DATE_FORMAT, Inputs as Inputs, PRESET_MODE_NA as PRESET_MODE_NA
from .errors import UnsupportedProperty as UnsupportedProperty
from .resources import AlexaCapabilityResource as AlexaCapabilityResource, AlexaGlobalCatalog as AlexaGlobalCatalog, AlexaModeResource as AlexaModeResource, AlexaPresetResource as AlexaPresetResource, AlexaSemantics as AlexaSemantics
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant.components import button as button, climate as climate, cover as cover, fan as fan, humidifier as humidifier, image_processing as image_processing, input_button as input_button, input_number as input_number, light as light, media_player as media_player, number as number, remote as remote, timer as timer, vacuum as vacuum, valve as valve, water_heater as water_heater
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat
from homeassistant.components.climate import HVACMode as HVACMode
from homeassistant.components.lock import LockState as LockState
from homeassistant.const import ATTR_CODE_FORMAT as ATTR_CODE_FORMAT, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_TEMPERATURE as ATTR_TEMPERATURE, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, PERCENTAGE as PERCENTAGE, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from typing import Any

_LOGGER: Incomplete
UNIT_TO_CATALOG_TAG: Incomplete

def get_resource_by_unit_of_measurement(entity: State) -> str: ...

class AlexaCapability:
    _resource: AlexaCapabilityResource | None
    _semantics: AlexaSemantics | None
    supported_locales: set[str]
    entity: Incomplete
    instance: Incomplete
    _non_controllable_properties: Incomplete
    def __init__(self, entity: State, instance: str | None = None, non_controllable_properties: bool | None = None) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def properties_non_controllable(self) -> bool | None: ...
    def get_property(self, name: str) -> dict[str, Any]: ...
    def supports_deactivation(self) -> bool | None: ...
    def capability_proactively_reported(self) -> bool | None: ...
    def capability_resources(self) -> dict[str, list[dict[str, Any]]]: ...
    def configuration(self) -> dict[str, Any] | None: ...
    def configurations(self) -> dict[str, Any] | None: ...
    def inputs(self) -> list[dict[str, str]] | None: ...
    def semantics(self) -> dict[str, Any] | None: ...
    def supported_operations(self) -> list[str]: ...
    def camera_stream_configurations(self) -> list[dict[str, Any]] | None: ...
    def serialize_discovery(self) -> dict[str, Any]: ...
    def serialize_properties(self) -> Generator[dict[str, Any]]: ...

class Alexa(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...

class AlexaEndpointHealth(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaPowerController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaLockController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_retrievable(self) -> bool: ...
    def properties_proactively_reported(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaSceneController(AlexaCapability):
    supported_locales: Incomplete
    _supports_deactivation: Incomplete
    def __init__(self, entity: State, supports_deactivation: bool) -> None: ...
    def supports_deactivation(self) -> bool | None: ...
    def name(self) -> str: ...

class AlexaBrightnessController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaColorController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaColorTemperatureController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaSpeaker(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaStepSpeaker(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...

class AlexaPlaybackController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def supported_operations(self) -> list[str]: ...

class AlexaInputController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def inputs(self) -> list[dict[str, str]] | None: ...
    @staticmethod
    def get_valid_inputs(source_list: list[Any]) -> list[dict[str, str]]: ...

class AlexaTemperatureSensor(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaContactSensor(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaMotionSensor(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaThermostatController(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def configuration(self) -> dict[str, Any] | None: ...

class AlexaPowerLevelController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaSecurityPanelController(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def configuration(self) -> dict[str, Any] | None: ...

class AlexaModeController(AlexaCapability):
    supported_locales: Incomplete
    _resource: Incomplete
    _semantics: Incomplete
    def __init__(self, entity: State, instance: str, non_controllable: bool = False) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def configuration(self) -> dict[str, Any] | None: ...
    def capability_resources(self) -> dict[str, list[dict[str, Any]]]: ...
    def semantics(self) -> dict[str, Any] | None: ...

class AlexaRangeController(AlexaCapability):
    supported_locales: Incomplete
    _resource: Incomplete
    _semantics: Incomplete
    def __init__(self, entity: State, instance: str | None, non_controllable: bool = False) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def configuration(self) -> dict[str, Any] | None: ...
    def capability_resources(self) -> dict[str, list[dict[str, Any]]]: ...
    def semantics(self) -> dict[str, Any] | None: ...

class AlexaToggleController(AlexaCapability):
    supported_locales: Incomplete
    _resource: Incomplete
    _semantics: Incomplete
    def __init__(self, entity: State, instance: str, non_controllable: bool = False) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def capability_resources(self) -> dict[str, list[dict[str, Any]]]: ...

class AlexaChannelController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...

class AlexaDoorbellEventSource(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def capability_proactively_reported(self) -> bool: ...

class AlexaPlaybackStateReporter(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...

class AlexaSeekController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...

class AlexaEventDetectionSensor(AlexaCapability):
    supported_locales: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, entity: State) -> None: ...
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_proactively_reported(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def configuration(self) -> dict[str, Any] | None: ...

class AlexaEqualizerController(AlexaCapability):
    supported_locales: Incomplete
    VALID_SOUND_MODES: Incomplete
    def name(self) -> str: ...
    def properties_supported(self) -> list[dict[str, str]]: ...
    def properties_retrievable(self) -> bool: ...
    def get_property(self, name: str) -> Any: ...
    def configurations(self) -> dict[str, Any] | None: ...
    @classmethod
    def get_valid_inputs(cls, sound_mode_list: list[str]) -> list[dict[str, str]]: ...

class AlexaTimeHoldController(AlexaCapability):
    supported_locales: Incomplete
    _allow_remote_resume: Incomplete
    def __init__(self, entity: State, allow_remote_resume: bool = False) -> None: ...
    def name(self) -> str: ...
    def configuration(self) -> dict[str, Any] | None: ...

class AlexaCameraStreamController(AlexaCapability):
    supported_locales: Incomplete
    def name(self) -> str: ...
    def camera_stream_configurations(self) -> list[dict[str, Any]] | None: ...
