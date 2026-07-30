from . import PROP_TO_ATTR as PROP_TO_ATTR
from .const import MediaPlayerEntityStateAttribute as MediaPlayerEntityStateAttribute
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_valid_float as check_valid_float
from typing import Any

INSIGNIFICANT_ATTRIBUTES: set[MediaPlayerEntityStateAttribute]
SIGNIFICANT_ATTRIBUTES: set[MediaPlayerEntityStateAttribute]

@callback
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> bool | None: ...
