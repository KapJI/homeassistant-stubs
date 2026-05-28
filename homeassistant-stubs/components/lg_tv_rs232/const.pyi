from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from lg_rs232_tv import LGTV

LOGGER: Incomplete
DOMAIN: str
CONF_SET_ID: str
QUERY_ATTRIBUTES: Incomplete
type LGTVRS232ConfigEntry = ConfigEntry[LGTV]
