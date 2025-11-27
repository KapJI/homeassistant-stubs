from .const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_DEVICE_NAME as CONF_DEVICE_NAME, CONF_ENERGYID_KEY as CONF_ENERGYID_KEY, CONF_HA_ENTITY_UUID as CONF_HA_ENTITY_UUID, CONF_PROVISIONING_KEY as CONF_PROVISIONING_KEY, CONF_PROVISIONING_SECRET as CONF_PROVISIONING_SECRET, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from energyid_webhooks.client_v2 import WebhookClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_track_entity_registry_updated_event as async_track_entity_registry_updated_event, async_track_state_change_event as async_track_state_change_event, async_track_time_interval as async_track_time_interval

_LOGGER: Incomplete
type EnergyIDConfigEntry = ConfigEntry[EnergyIDRuntimeData]
DEFAULT_UPLOAD_INTERVAL_SECONDS: int

@dataclass
class EnergyIDRuntimeData:
    client: WebhookClient
    mappings: dict[str, str]
    state_listener: CALLBACK_TYPE | None = ...
    registry_tracking_listener: CALLBACK_TYPE | None = ...
    unavailable_logged: bool = ...

async def async_setup_entry(hass: HomeAssistant, entry: EnergyIDConfigEntry) -> bool: ...
async def config_entry_update_listener(hass: HomeAssistant, entry: EnergyIDConfigEntry) -> None: ...
@callback
def update_listeners(hass: HomeAssistant, entry: EnergyIDConfigEntry) -> None: ...
@callback
def _async_handle_state_change(hass: HomeAssistant, entry_id: str, event: Event[EventStateChangedData]) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: EnergyIDConfigEntry) -> bool: ...
