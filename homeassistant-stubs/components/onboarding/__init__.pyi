from . import views as views
from .const import DOMAIN as DOMAIN, STEPS as STEPS, STEP_ANALYTICS as STEP_ANALYTICS, STEP_CORE_CONFIG as STEP_CORE_CONFIG, STEP_INTEGRATION as STEP_INTEGRATION, STEP_USER as STEP_USER
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass

STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
CONFIG_SCHEMA: Incomplete

class OnboadingStorage(Store[dict[str, list[str]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[str]]) -> dict[str, list[str]]: ...

def async_is_onboarded(hass: HomeAssistant) -> bool: ...
def async_is_user_onboarded(hass: HomeAssistant) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
