from .util import OTBRData as OTBRData
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type OTBRConfigEntry = ConfigEntry[OTBRData]
