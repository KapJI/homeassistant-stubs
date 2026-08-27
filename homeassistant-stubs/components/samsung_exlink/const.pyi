from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from samsung_exlink import SamsungTV

LOGGER: Incomplete
DOMAIN: str
type SamsungExLinkConfigEntry = ConfigEntry[SamsungTV]
