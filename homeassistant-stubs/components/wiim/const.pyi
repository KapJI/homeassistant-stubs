from .models import WiimData as WiimData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final
from wiim import WiimDevice

type WiimConfigEntry = ConfigEntry[WiimDevice]
DOMAIN: Final[str]
LOGGER: Incomplete
DATA_WIIM: HassKey[WiimData]
PLATFORMS: Final[list[Platform]]
UPNP_PORT: int
ZEROCONF_TYPE_LINKPLAY: Final[str]
