from _typeshed import Incomplete
from homeassistant.components import onboarding as onboarding
from homeassistant.components.lovelace import _create_map_dashboard as _create_map_dashboard
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
CONFIG_SCHEMA: Incomplete
STORAGE_KEY = DOMAIN
STORAGE_VERSION_MAJOR: int

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
