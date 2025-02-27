from .const import DEFAULT_PORT as DEFAULT_PORT
from .errors import TemporaryFailure as TemporaryFailure, ValidationFailure as ValidationFailure
from .helper import get_cert_expiry_timestamp as get_cert_expiry_timestamp
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type CertExpiryConfigEntry = ConfigEntry[CertExpiryDataUpdateCoordinator]

class CertExpiryDataUpdateCoordinator(DataUpdateCoordinator[datetime | None]):
    config_entry: CertExpiryConfigEntry
    host: Incomplete
    port: Incomplete
    cert_error: ValidationFailure | None
    is_cert_valid: bool
    def __init__(self, hass: HomeAssistant, config_entry: CertExpiryConfigEntry, host: str, port: int) -> None: ...
    async def _async_update_data(self) -> datetime | None: ...
