from _typeshed import Incomplete
from homeassistant.components.climate import HVACAction as HVACAction, HVACMode as HVACMode, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from visionpluspython.models import ThermostatMode

DOMAIN: str
OAUTH2_AUTHORIZE: str
OAUTH2_TOKEN: str
OAUTH2_SCOPES: Incomplete
UPDATE_INTERVAL_SECONDS: int
FAST_POLLING_INTERVAL_SECONDS: int
DISCOVERY_INTERVAL_MINUTES: int
THERMOSTAT_MODE_TO_HVAC: dict[ThermostatMode, HVACMode]
HVAC_MODE_TO_THERMOSTAT: dict[HVACMode, ThermostatMode]
PRESET_MODES: list[str]
THERMOSTAT_MODE_TO_PRESET: dict[ThermostatMode, str]
PRESET_MODE_TO_THERMOSTAT: dict[str, ThermostatMode]
HVAC_ACTION_TO_HA: dict[str, HVACAction]
SUPPORTED_DEVICE_TYPES: Incomplete
SERVICE_ACTIVATE_TIMER_MODE: str
ATTR_DURATION: str
