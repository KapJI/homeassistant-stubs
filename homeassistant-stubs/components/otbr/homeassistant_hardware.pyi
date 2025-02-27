from .const import DOMAIN as DOMAIN
from .types import OTBRConfigEntry as OTBRConfigEntry
from _typeshed import Incomplete
from homeassistant.components.hassio import AddonManager as AddonManager
from homeassistant.components.homeassistant_hardware.util import ApplicationType as ApplicationType, FirmwareInfo as FirmwareInfo, OwningAddon as OwningAddon, OwningIntegration as OwningIntegration, get_otbr_addon_firmware_info as get_otbr_addon_firmware_info
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.hassio import is_hassio as is_hassio

_LOGGER: Incomplete

async def async_get_firmware_info(hass: HomeAssistant, config_entry: OTBRConfigEntry) -> FirmwareInfo | None: ...
