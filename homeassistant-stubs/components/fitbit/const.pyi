from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from typing import Final

ATTR_ACCESS_TOKEN: Final[str]
ATTR_REFRESH_TOKEN: Final[str]
ATTR_LAST_SAVED_AT: Final[str]
ATTR_DURATION: Final[str]
ATTR_DISTANCE: Final[str]
ATTR_ELEVATION: Final[str]
ATTR_HEIGHT: Final[str]
ATTR_WEIGHT: Final[str]
ATTR_BODY: Final[str]
ATTR_LIQUIDS: Final[str]
ATTR_BLOOD_GLUCOSE: Final[str]
ATTR_BATTERY: Final[str]
CONF_MONITORED_RESOURCES: Final[str]
CONF_CLOCK_FORMAT: Final[str]
ATTRIBUTION: Final[str]
FITBIT_AUTH_CALLBACK_PATH: Final[str]
FITBIT_AUTH_START: Final[str]
FITBIT_CONFIG_FILE: Final[str]
FITBIT_DEFAULT_RESOURCES: Final[list[str]]
DEFAULT_CONFIG: Final[dict[str, str]]
DEFAULT_CLOCK_FORMAT: Final[str]

class FitbitSensorEntityDescription(SensorEntityDescription):
    unit_type: str | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, unit_type) -> None: ...

FITBIT_RESOURCES_LIST: Final[tuple[FitbitSensorEntityDescription, ...]]
FITBIT_RESOURCE_BATTERY: Incomplete
FITBIT_RESOURCES_KEYS: Final[list[str]]
FITBIT_MEASUREMENTS: Final[dict[str, dict[str, str]]]
BATTERY_LEVELS: Final[dict[str, int]]
