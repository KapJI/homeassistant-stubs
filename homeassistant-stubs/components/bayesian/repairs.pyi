from . import DOMAIN as DOMAIN
from .helpers import Observation as Observation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import issue_registry as issue_registry

def raise_mirrored_entries(hass: HomeAssistant, observations: list[Observation], text: str = ...) -> None: ...
def raise_no_prob_given_false(hass: HomeAssistant, text: str) -> None: ...