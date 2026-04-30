from .const import ADDON_SLUG as ADDON_SLUG, CONF_ADDON_LR_S2_ACCESS_CONTROL_KEY as CONF_ADDON_LR_S2_ACCESS_CONTROL_KEY, CONF_ADDON_LR_S2_AUTHENTICATED_KEY as CONF_ADDON_LR_S2_AUTHENTICATED_KEY, CONF_ADDON_NETWORK_KEY as CONF_ADDON_NETWORK_KEY, CONF_ADDON_S0_LEGACY_KEY as CONF_ADDON_S0_LEGACY_KEY, CONF_ADDON_S2_ACCESS_CONTROL_KEY as CONF_ADDON_S2_ACCESS_CONTROL_KEY, CONF_ADDON_S2_AUTHENTICATED_KEY as CONF_ADDON_S2_AUTHENTICATED_KEY, CONF_ADDON_S2_UNAUTHENTICATED_KEY as CONF_ADDON_S2_UNAUTHENTICATED_KEY, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.hassio import AddonError as AddonError, AddonManager as AddonManager
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.redact import async_redact_data as async_redact_data
from homeassistant.helpers.singleton import singleton as singleton
from typing import Any

DATA_ADDON_MANAGER: Incomplete
REDACT_ADDON_OPTION_KEYS: Incomplete

def _redact_sensitive_option_values(message: str, config: dict[str, Any]) -> str: ...

class ZwaveAddonManager(AddonManager):
    async def async_set_addon_options(self, config: dict[str, Any]) -> None: ...

@callback
def get_addon_manager(hass: HomeAssistant) -> AddonManager: ...
