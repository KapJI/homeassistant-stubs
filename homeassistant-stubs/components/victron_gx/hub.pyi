from .const import CONF_INSTALLATION_ID as CONF_INSTALLATION_ID, CONF_MODEL as CONF_MODEL, CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.redact import async_redact_data as async_redact_data
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, Hub as VictronVenusHub, Metric as VictronVenusMetric, MetricKind as MetricKind

_LOGGER: Incomplete
UPDATE_INTERVAL_SECONDS: int
TO_REDACT: Incomplete
type VictronGxConfigEntry = ConfigEntry[Hub]
NewMetricCallback = Callable[[VictronVenusDevice, VictronVenusMetric, DeviceInfo, str], None]

class Hub:
    hass: Incomplete
    host: Incomplete
    _hub: Incomplete
    new_metric_callbacks: dict[MetricKind, NewMetricCallback]
    def __init__(self, hass: HomeAssistant, entry: VictronGxConfigEntry) -> None: ...
    async def start(self) -> None: ...
    async def stop(self) -> None: ...
    def _on_new_metric(self, hub: VictronVenusHub, device: VictronVenusDevice, metric: VictronVenusMetric) -> None: ...
    @staticmethod
    def _map_device_info(device: VictronVenusDevice, installation_id: str) -> DeviceInfo: ...
    def is_device_connected(self, device_identifiers: set[tuple[str, str]]) -> bool: ...
    def get_diagnostics_data(self) -> dict[str, Any]: ...
    def register_new_metric_callback(self, kind: MetricKind, new_metric_callback: NewMetricCallback) -> None: ...
    def unregister_all_new_metric_callbacks(self) -> None: ...
