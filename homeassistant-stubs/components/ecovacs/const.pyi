from _typeshed import Incomplete
from enum import StrEnum

DOMAIN: str
CONF_CONTINENT: str
CONF_OVERRIDE_REST_URL: str
CONF_OVERRIDE_MQTT_URL: str
CONF_VERIFY_MQTT_CERTIFICATE: str
SUPPORTED_LIFESPANS: Incomplete

class InstanceMode(StrEnum):
    CLOUD: str
    SELF_HOSTED: str
