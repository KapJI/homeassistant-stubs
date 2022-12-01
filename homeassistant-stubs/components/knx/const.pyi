from _typeshed import Incomplete
from enum import Enum
from homeassistant.components.climate import HVACAction as HVACAction, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE, PRESET_SLEEP as PRESET_SLEEP
from homeassistant.const import Platform as Platform
from typing import Final, TypedDict

DOMAIN: Final[str]
KNX_ADDRESS: Final[str]
CONF_INVERT: Final[str]
CONF_KNX_EXPOSE: Final[str]
CONF_KNX_INDIVIDUAL_ADDRESS: Final[str]
CONF_KNX_CONNECTION_TYPE: Final[str]
CONF_KNX_AUTOMATIC: Final[str]
CONF_KNX_ROUTING: Final[str]
CONF_KNX_ROUTING_BACKBONE_KEY: Final[str]
CONF_KNX_ROUTING_SYNC_LATENCY_TOLERANCE: Final[str]
CONF_KNX_ROUTING_SECURE: Final[str]
CONF_KNX_TUNNELING: Final[str]
CONF_KNX_TUNNELING_TCP: Final[str]
CONF_KNX_TUNNELING_TCP_SECURE: Final[str]
CONF_KNX_LOCAL_IP: Final[str]
CONF_KNX_MCAST_GRP: Final[str]
CONF_KNX_MCAST_PORT: Final[str]
CONF_KNX_RATE_LIMIT: Final[str]
CONF_KNX_ROUTE_BACK: Final[str]
CONF_KNX_STATE_UPDATER: Final[str]
CONF_KNX_DEFAULT_STATE_UPDATER: Final[bool]
CONF_KNX_DEFAULT_RATE_LIMIT: Final[int]
DEFAULT_ROUTING_IA: Final[str]
CONST_KNX_STORAGE_KEY: Final[str]
CONF_KNX_KNXKEY_FILENAME: Final[str]
CONF_KNX_KNXKEY_PASSWORD: Final[str]
CONF_KNX_SECURE_USER_ID: Final[str]
CONF_KNX_SECURE_USER_PASSWORD: Final[str]
CONF_KNX_SECURE_DEVICE_AUTHENTICATION: Final[str]
CONF_PAYLOAD: Final[str]
CONF_PAYLOAD_LENGTH: Final[str]
CONF_RESET_AFTER: Final[str]
CONF_RESPOND_TO_READ: Final[str]
CONF_STATE_ADDRESS: Final[str]
CONF_SYNC_STATE: Final[str]
DATA_KNX_CONFIG: Final[str]
DATA_HASS_CONFIG: Final[str]
ATTR_COUNTER: Final[str]
ATTR_SOURCE: Final[str]

class KNXConfigEntryData(TypedDict):
    connection_type: str
    individual_address: str
    local_ip: Union[str, None]
    multicast_group: str
    multicast_port: int
    route_back: bool
    state_updater: bool
    rate_limit: int
    host: str
    port: int
    user_id: Union[int, None]
    user_password: Union[str, None]
    device_authentication: Union[str, None]
    knxkeys_filename: str
    knxkeys_password: str
    backbone_key: Union[str, None]
    sync_latency_tolerance: Union[int, None]

class ColorTempModes(Enum):
    ABSOLUTE: str
    RELATIVE: str

SUPPORTED_PLATFORMS: Final[Incomplete]
CONTROLLER_MODES: Final[Incomplete]
CURRENT_HVAC_ACTIONS: Final[Incomplete]
PRESET_MODES: Final[Incomplete]
