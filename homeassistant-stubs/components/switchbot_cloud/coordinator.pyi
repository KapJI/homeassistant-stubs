from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from switchbot_api import Device as Device, Remote, SwitchBotAPI as SwitchBotAPI
from typing import Any

_LOGGER: Incomplete
type Status = dict[str, Any] | None

class SwitchBotCoordinator(DataUpdateCoordinator[Status]):
    config_entry: ConfigEntry
    _api: SwitchBotAPI
    _device_id: str
    _manageable_by_webhook: bool
    _webhooks_connected: bool
    _should_poll: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: SwitchBotAPI, device: Device | Remote, manageable_by_webhook: bool) -> None: ...
    update_interval: Incomplete
    def webhook_subscription_listener(self, connected: bool) -> None: ...
    def manageable_by_webhook(self) -> bool: ...
    async def _async_update_data(self) -> Status: ...
