from _typeshed import Incomplete
from airgradient import ApiVersion, Config as Config
from dataclasses import dataclass

DOMAIN: str
LOGGER: Incomplete
PM_STANDARD: Incomplete
PM_STANDARD_REVERSE: Incomplete
CONFIGURATION_CONTROL: str
CO2_ABC: str
NOX_LEARNING_OFFSET: str
TVOC_LEARNING_OFFSET: str
POST_DATA: str
PM_STANDARD_CONFIG: str
TEMPERATURE_UNIT: str
LED_BAR_MODE: str
LED_BAR_BRIGHTNESS: str
DISPLAY_BRIGHTNESS: str
GPS_MODE: str
FRONT_LED_BRIGHTNESS: str
BACK_LED_BRIGHTNESS: str
TOUCH_LED_INTENSITY: str
BUZZER_ENABLED: str
CLOUD_CONNECTION: str
CO2_CALIBRATION: str
LED_BAR_TEST: str

@dataclass(frozen=True, kw_only=True)
class ModelCapabilities:
    config: frozenset[str]
    actions: frozenset[str]

COMMON_LEGACY_CONFIG: Incomplete
GO_CONFIG: Incomplete
OUTDOOR_CAPABILITIES: Incomplete
MODEL_CAPABILITIES: tuple[tuple[str, ModelCapabilities], ...]

def get_model_capabilities(model: str) -> ModelCapabilities | None: ...
def supports_config(model: str, api_version: ApiVersion | None, config: Config, capability: str) -> bool: ...
def supports_action(model: str, action: str) -> bool: ...
