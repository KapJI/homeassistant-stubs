from .const import ATTR_FLAP_ID as ATTR_FLAP_ID, ATTR_LOCK_STATE as ATTR_LOCK_STATE, ATTR_PET_NAME as ATTR_PET_NAME, DOMAIN as DOMAIN, SERVICE_SET_LOCK_STATE as SERVICE_SET_LOCK_STATE, SERVICE_SET_PET_LOCATION as SERVICE_SET_PET_LOCATION
from .coordinator import SurePetcareConfigEntry as SurePetcareConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import service as service

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
