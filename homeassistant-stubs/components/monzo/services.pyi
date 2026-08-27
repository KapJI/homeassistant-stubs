from .const import DEVICE_MODEL_ACCOUNT as DEVICE_MODEL_ACCOUNT, DEVICE_MODEL_POT as DEVICE_MODEL_POT, DOMAIN as DOMAIN, NON_TRANSFER_ACCOUNT_TYPES as NON_TRANSFER_ACCOUNT_TYPES
from .coordinator import MonzoConfigEntry as MonzoConfigEntry, MonzoCoordinator as MonzoCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import device_registry as dr, selector as selector, service as service
from monzopy import InvalidMonzoAPIResponseError
from typing import Any, Final

ATTR_ACCOUNT: Final[str]
ATTR_AMOUNT: Final[str]
ATTR_POT: Final[str]
SERVICE_DEPOSIT_INTO_POT: Final[str]
SERVICE_WITHDRAW_FROM_POT: Final[str]
type TransferFunction = Callable[[str, str, int], Awaitable[bool]]

def _amount_to_minor_units(value: Any) -> int: ...
def _transfer_rejection_reason(error: InvalidMonzoAPIResponseError) -> str | None: ...

TRANSFER_SCHEMA: Incomplete

@callback
def _async_get_device(call: ServiceCall, field: str) -> dr.AnyDeviceEntry: ...
@callback
def _async_get_resource_id(device: dr.AnyDeviceEntry) -> str: ...
def _device_name(device: dr.AnyDeviceEntry) -> str: ...
@callback
def _async_resolve_transfer(call: ServiceCall) -> tuple[MonzoCoordinator, str, str]: ...
async def _async_transfer(call: ServiceCall, transfer_fn: Callable[[MonzoCoordinator], TransferFunction]) -> None: ...
async def _async_deposit_into_pot(call: ServiceCall) -> None: ...
async def _async_withdraw_from_pot(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
