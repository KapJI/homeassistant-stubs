from .models import HaZeroconf as HaZeroconf
from homeassistant.helpers.frame import report as report

def install_multiple_zeroconf_catcher(hass_zc: HaZeroconf) -> None: ...
