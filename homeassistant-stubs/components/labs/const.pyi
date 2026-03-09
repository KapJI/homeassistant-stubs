from .models import LabsData as LabsData
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
STORAGE_KEY: str
STORAGE_VERSION: int
LABS_DATA: HassKey[LabsData]
