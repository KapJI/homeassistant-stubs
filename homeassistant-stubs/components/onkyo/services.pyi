from .const import DOMAIN as DOMAIN, LEGACY_REV_HDMI_OUTPUT_MAPPING as LEGACY_REV_HDMI_OUTPUT_MAPPING
from .media_player import OnkyoMediaPlayer as OnkyoMediaPlayer
from _typeshed import Incomplete
from aioonkyo import Zone as Zone
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_MP_ENTITIES: HassKey[dict[str, dict[Zone, OnkyoMediaPlayer]]]
ATTR_HDMI_OUTPUT: str
ONKYO_SELECT_OUTPUT_SCHEMA: Incomplete
SERVICE_SELECT_HDMI_OUTPUT: str

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
