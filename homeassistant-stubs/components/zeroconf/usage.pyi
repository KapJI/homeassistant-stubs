from .models import HaZeroconf as HaZeroconf
from homeassistant.helpers.frame import MissingIntegrationFrame as MissingIntegrationFrame, get_integration_frame as get_integration_frame, report_integration as report_integration

def install_multiple_zeroconf_catcher(hass_zc: HaZeroconf) -> None: ...
