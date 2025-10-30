from _typeshed import Incomplete
from datapoint.Forecast import Forecast as Forecast
from datapoint.Manager import Manager as Manager
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from typing import Any, Literal

_LOGGER: Incomplete

def fetch_data(connection: Manager, latitude: float, longitude: float, frequency: Literal['daily', 'twice-daily', 'hourly']) -> Forecast: ...
def get_attribute(data: dict[str, Any] | None, attr_name: str) -> Any | None: ...
