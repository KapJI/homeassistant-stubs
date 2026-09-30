from .models import TRIGGERS as TRIGGERS
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.const import CONF_SELECTOR as CONF_SELECTOR
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import selector as selector
from homeassistant.helpers.automation import get_absolute_description_key as get_absolute_description_key
from homeassistant.helpers.selector import TargetSelector as TargetSelector
from homeassistant.loader import Integration as Integration, async_get_integrations as async_get_integrations
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.yaml import load_yaml_dict as load_yaml_dict
from typing import Any

_LOGGER: Incomplete
TRIGGER_DESCRIPTION_CACHE: HassKey[dict[str, dict[str, Any] | None]]
_FIELD_DESCRIPTION_SCHEMA: Incomplete
_TRIGGER_DESCRIPTION_SCHEMA: Incomplete

def starts_with_dot(key: str) -> str: ...

_TRIGGERS_DESCRIPTION_SCHEMA: Incomplete

def _load_triggers_file(integration: Integration) -> dict[str, Any]: ...
def _load_triggers_files(integrations: Iterable[Integration]) -> dict[str, dict[str, Any]]: ...
async def async_get_all_descriptions(hass: HomeAssistant) -> dict[str, dict[str, Any] | None]: ...
