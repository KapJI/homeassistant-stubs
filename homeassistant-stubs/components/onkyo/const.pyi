from _typeshed import Incomplete
from aioonkyo import HDMIOutputParam, InputSourceParam, ListeningModeParam
from typing import Literal

DOMAIN: str
DEVICE_INTERVIEW_TIMEOUT: int
DEVICE_DISCOVERY_TIMEOUT: int
type VolumeResolution = Literal[50, 80, 100, 200]
OPTION_VOLUME_RESOLUTION: str
OPTION_VOLUME_RESOLUTION_DEFAULT: VolumeResolution
VOLUME_RESOLUTION_ALLOWED: tuple[VolumeResolution, ...]
OPTION_MAX_VOLUME: str
OPTION_MAX_VOLUME_DEFAULT: float
OPTION_INPUT_SOURCES: str
OPTION_LISTENING_MODES: str
InputSource = InputSourceParam
ListeningMode = ListeningModeParam
HDMIOutput = HDMIOutputParam
ZONES: Incomplete
LEGACY_HDMI_OUTPUT_MAPPING: Incomplete
LEGACY_REV_HDMI_OUTPUT_MAPPING: Incomplete
