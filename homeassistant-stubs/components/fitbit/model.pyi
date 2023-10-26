from .const import CONF_CLOCK_FORMAT as CONF_CLOCK_FORMAT, CONF_MONITORED_RESOURCES as CONF_MONITORED_RESOURCES, FitbitScope as FitbitScope
from collections.abc import Mapping
from typing import Any

class FitbitProfile:
    encoded_id: str
    full_name: str
    locale: str | None
    def __init__(self, encoded_id, full_name, locale) -> None: ...

class FitbitDevice:
    id: str
    device_version: str
    battery_level: int
    battery: str
    type: str
    def __init__(self, id, device_version, battery_level, battery, type) -> None: ...

class FitbitConfig:
    clock_format: str | None
    monitored_resources: set[str] | None
    scopes: set[FitbitScope]
    def is_explicit_enable(self, key: str) -> bool: ...
    def is_allowed_resource(self, scope: FitbitScope | None, key: str) -> bool: ...
    def __init__(self, clock_format, monitored_resources, scopes) -> None: ...

def config_from_entry_data(data: Mapping[str, Any]) -> FitbitConfig: ...
