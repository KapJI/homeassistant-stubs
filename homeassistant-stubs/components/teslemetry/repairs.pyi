from . import TeslemetryConfigEntry as TeslemetryConfigEntry, _async_get_rsa_key_pem as _async_get_rsa_key_pem
from .const import ISSUE_GATEWAY_NOT_FOUND as ISSUE_GATEWAY_NOT_FOUND, LOGGER as LOGGER, VEHICLE_ISSUE_LEARN_MORE as VEHICLE_ISSUE_LEARN_MORE
from .helpers import PowerwallKeyRejectedError as PowerwallKeyRejectedError, async_verify_local_gateway as async_verify_local_gateway, cloud_energy_site as cloud_energy_site
from _typeshed import Incomplete
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

class VehicleMetadataRepairFlow(RepairsFlow):
    entry: Incomplete
    vin: Incomplete
    issue_type: Incomplete
    placeholders: Incomplete
    def __init__(self, entry: TeslemetryConfigEntry, vin: str, issue_type: str, vehicle: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...

class GatewayNotFoundRepairFlow(RepairsFlow):
    entry_id: Incomplete
    subentry_id: Incomplete
    _entry: TeslemetryConfigEntry | None
    _subentry: ConfigSubentry | None
    _key_pem: bytes
    _default_host: str
    def __init__(self, entry_id: str, subentry_id: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> RepairsFlowResult: ...
    async def async_step_host(self, user_input: dict[str, Any] | None = None) -> RepairsFlowResult: ...
    @callback
    def _async_show_host_form(self, errors: dict[str, str]) -> RepairsFlowResult: ...
    async def _async_verify(self, host: str) -> str | None: ...
    @callback
    def _async_save_host(self, host: str) -> RepairsFlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
