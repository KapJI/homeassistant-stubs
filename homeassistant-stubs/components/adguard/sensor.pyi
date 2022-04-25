from . import AdGuardHomeDeviceEntity as AdGuardHomeDeviceEntity
from .const import DATA_ADGUARD_CLIENT as DATA_ADGUARD_CLIENT, DATA_ADGUARD_VERSION as DATA_ADGUARD_VERSION, DOMAIN as DOMAIN
from adguardhome import AdGuardHome as AdGuardHome
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TIME_MILLISECONDS as TIME_MILLISECONDS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SCAN_INTERVAL: Any
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AdGuardHomeSensor(AdGuardHomeDeviceEntity, SensorEntity):
    _state: Any
    _unit_of_measurement: Any
    measurement: Any
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry, name: str, icon: str, measurement: str, unit_of_measurement: str, enabled_default: bool = ...) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def native_value(self) -> Union[int, str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class AdGuardHomeDNSQueriesSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomeBlockedFilteringSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomePercentageBlockedSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomeReplacedParentalSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomeReplacedSafeBrowsingSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomeReplacedSafeSearchSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomeAverageProcessingTimeSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...

class AdGuardHomeRulesCountSensor(AdGuardHomeSensor):
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    _state: Any
    async def _adguard_update(self) -> None: ...