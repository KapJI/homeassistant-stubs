from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import Platform as Platform
from typing import Final

DOMAIN: Final[str]
ENTRY_TITLE: str
DEFAULT_SCAN_INTERVAL: Incomplete
CONF_CLOUDHOOK_URL: Final[str]
SENSOR_KIND_TEMPERATURE: str
SENSOR_KIND_HUMIDITY: str
SENSOR_KIND_BATTERY: str
VACUUM_FAN_SPEED_QUIET: str
VACUUM_FAN_SPEED_STANDARD: str
VACUUM_FAN_SPEED_STRONG: str
VACUUM_FAN_SPEED_MAX: str
CLIMATE_PRESET_SCHEDULE: str
AI_ART_FRAME_UPLOAD_IMAGE_SERVICE: str
AFTER_COMMAND_REFRESH: int
COVER_ENTITY_AFTER_COMMAND_REFRESH: int
SMART_RADIATOR_THERMOSTAT_AFTER_COMMAND_REFRESH: int
HUMIDITY_LEVELS: Incomplete
NIGHT_LIGHT_ON: str
NIGHT_LIGHT_OFF: str
NIGHT_LIGHT_BRIGHT: str
NIGHT_LIGHT_SOFT: str
STANDING_FAN_NIGHT_LIGHT_PARAMETERS_MAP: Incomplete
BATTERY_CIRCULATOR_FAN_2_PRO_NIGHT_LIGHT_PARAMETERS_MAP: Incomplete

@dataclass(frozen=True)
class SwitchbotCloudDeviceConfig:
    webhook: bool
    entity_config: tuple[Platform, ...]

DEVICE_SUPPORT_MAP: Final[dict[str, SwitchbotCloudDeviceConfig]]
