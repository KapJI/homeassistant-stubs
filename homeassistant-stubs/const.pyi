from _typeshed import Incomplete
from enum import StrEnum
from typing import Final

APPLICATION_NAME: Final[str]
MAJOR_VERSION: Final[int]
MINOR_VERSION: Final[int]
PATCH_VERSION: Final[str]
__short_version__: Final[Incomplete]
__version__: Final[Incomplete]
REQUIRED_PYTHON_VER: Final[tuple[int, int, int]]
REQUIRED_NEXT_PYTHON_VER: Final[tuple[int, int, int]]
REQUIRED_NEXT_PYTHON_HA_RELEASE: Final[str]
PLATFORM_FORMAT: Final[str]

class Platform(StrEnum):
    AIR_QUALITY: str
    ALARM_CONTROL_PANEL: str
    BINARY_SENSOR: str
    BUTTON: str
    CALENDAR: str
    CAMERA: str
    CLIMATE: str
    COVER: str
    DATE: str
    DATETIME: str
    DEVICE_TRACKER: str
    EVENT: str
    FAN: str
    GEO_LOCATION: str
    HUMIDIFIER: str
    IMAGE: str
    IMAGE_PROCESSING: str
    LIGHT: str
    LOCK: str
    MAILBOX: str
    MEDIA_PLAYER: str
    NOTIFY: str
    NUMBER: str
    REMOTE: str
    SCENE: str
    SELECT: str
    SENSOR: str
    SIREN: str
    STT: str
    SWITCH: str
    TEXT: str
    TIME: str
    TTS: str
    VACUUM: str
    UPDATE: str
    WATER_HEATER: str
    WEATHER: str

MATCH_ALL: Final[str]
ENTITY_MATCH_NONE: Final[str]
ENTITY_MATCH_ALL: Final[str]
ENTITY_MATCH_ANY: Final[str]
DEVICE_DEFAULT_NAME: Final[str]
MAX_LENGTH_EVENT_EVENT_TYPE: Final[int]
MAX_LENGTH_EVENT_ORIGIN: Final[int]
MAX_LENGTH_EVENT_CONTEXT_ID: Final[int]
MAX_LENGTH_STATE_DOMAIN: Final[int]
MAX_LENGTH_STATE_ENTITY_ID: Final[int]
MAX_LENGTH_STATE_STATE: Final[int]
SUN_EVENT_SUNSET: Final[str]
SUN_EVENT_SUNRISE: Final[str]
CONF_ABOVE: Final[str]
CONF_ACCESS_TOKEN: Final[str]
CONF_ADDRESS: Final[str]
CONF_AFTER: Final[str]
CONF_ALIAS: Final[str]
CONF_ALLOWLIST_EXTERNAL_URLS: Final[str]
CONF_API_KEY: Final[str]
CONF_API_TOKEN: Final[str]
CONF_API_VERSION: Final[str]
CONF_ARMING_TIME: Final[str]
CONF_AT: Final[str]
CONF_ATTRIBUTE: Final[str]
CONF_AUTH_MFA_MODULES: Final[str]
CONF_AUTH_PROVIDERS: Final[str]
CONF_AUTHENTICATION: Final[str]
CONF_BASE: Final[str]
CONF_BEFORE: Final[str]
CONF_BELOW: Final[str]
CONF_BINARY_SENSORS: Final[str]
CONF_BRIGHTNESS: Final[str]
CONF_BROADCAST_ADDRESS: Final[str]
CONF_BROADCAST_PORT: Final[str]
CONF_CHOOSE: Final[str]
CONF_CLIENT_ID: Final[str]
CONF_CLIENT_SECRET: Final[str]
CONF_CODE: Final[str]
CONF_COLOR_TEMP: Final[str]
CONF_COMMAND: Final[str]
CONF_COMMAND_CLOSE: Final[str]
CONF_COMMAND_OFF: Final[str]
CONF_COMMAND_ON: Final[str]
CONF_COMMAND_OPEN: Final[str]
CONF_COMMAND_STATE: Final[str]
CONF_COMMAND_STOP: Final[str]
CONF_CONDITION: Final[str]
CONF_CONDITIONS: Final[str]
CONF_CONTINUE_ON_ERROR: Final[str]
CONF_CONTINUE_ON_TIMEOUT: Final[str]
CONF_COUNT: Final[str]
CONF_COUNTRY: Final[str]
CONF_COVERS: Final[str]
CONF_CURRENCY: Final[str]
CONF_CUSTOMIZE: Final[str]
CONF_CUSTOMIZE_DOMAIN: Final[str]
CONF_CUSTOMIZE_GLOB: Final[str]
CONF_DEFAULT: Final[str]
CONF_DELAY: Final[str]
CONF_DELAY_TIME: Final[str]
CONF_DESCRIPTION: Final[str]
CONF_DEVICE: Final[str]
CONF_DEVICES: Final[str]
CONF_DEVICE_CLASS: Final[str]
CONF_DEVICE_ID: Final[str]
CONF_DISARM_AFTER_TRIGGER: Final[str]
CONF_DISCOVERY: Final[str]
CONF_DISKS: Final[str]
CONF_DISPLAY_CURRENCY: Final[str]
CONF_DISPLAY_OPTIONS: Final[str]
CONF_DOMAIN: Final[str]
CONF_DOMAINS: Final[str]
CONF_EFFECT: Final[str]
CONF_ELEVATION: Final[str]
CONF_ELSE: Final[str]
CONF_EMAIL: Final[str]
CONF_ENABLED: Final[str]
CONF_ENTITIES: Final[str]
CONF_ENTITY_CATEGORY: Final[str]
CONF_ENTITY_ID: Final[str]
CONF_ENTITY_NAMESPACE: Final[str]
CONF_ENTITY_PICTURE_TEMPLATE: Final[str]
CONF_ERROR: Final[str]
CONF_EVENT: Final[str]
CONF_EVENT_DATA: Final[str]
CONF_EVENT_DATA_TEMPLATE: Final[str]
CONF_EXCLUDE: Final[str]
CONF_EXTERNAL_URL: Final[str]
CONF_FILENAME: Final[str]
CONF_FILE_PATH: Final[str]
CONF_FOR: Final[str]
CONF_FOR_EACH: Final[str]
CONF_FORCE_UPDATE: Final[str]
CONF_FRIENDLY_NAME: Final[str]
CONF_FRIENDLY_NAME_TEMPLATE: Final[str]
CONF_HEADERS: Final[str]
CONF_HOST: Final[str]
CONF_HOSTS: Final[str]
CONF_HS: Final[str]
CONF_ICON: Final[str]
CONF_ICON_TEMPLATE: Final[str]
CONF_ID: Final[str]
CONF_IF: Final[str]
CONF_INCLUDE: Final[str]
CONF_INTERNAL_URL: Final[str]
CONF_IP_ADDRESS: Final[str]
CONF_LANGUAGE: Final[str]
CONF_LATITUDE: Final[str]
CONF_LEGACY_TEMPLATES: Final[str]
CONF_LIGHTS: Final[str]
CONF_LOCATION: Final[str]
CONF_LONGITUDE: Final[str]
CONF_MAC: Final[str]
CONF_MATCH: Final[str]
CONF_MAXIMUM: Final[str]
CONF_MEDIA_DIRS: Final[str]
CONF_METHOD: Final[str]
CONF_MINIMUM: Final[str]
CONF_MODE: Final[str]
CONF_MODEL: Final[str]
CONF_MONITORED_CONDITIONS: Final[str]
CONF_MONITORED_VARIABLES: Final[str]
CONF_NAME: Final[str]
CONF_OFFSET: Final[str]
CONF_OPTIMISTIC: Final[str]
CONF_PACKAGES: Final[str]
CONF_PARALLEL: Final[str]
CONF_PARAMS: Final[str]
CONF_PASSWORD: Final[str]
CONF_PATH: Final[str]
CONF_PAYLOAD: Final[str]
CONF_PAYLOAD_OFF: Final[str]
CONF_PAYLOAD_ON: Final[str]
CONF_PENDING_TIME: Final[str]
CONF_PIN: Final[str]
CONF_PLATFORM: Final[str]
CONF_PORT: Final[str]
CONF_PREFIX: Final[str]
CONF_PROFILE_NAME: Final[str]
CONF_PROTOCOL: Final[str]
CONF_PROXY_SSL: Final[str]
CONF_QUOTE: Final[str]
CONF_RADIUS: Final[str]
CONF_RECIPIENT: Final[str]
CONF_REGION: Final[str]
CONF_REPEAT: Final[str]
CONF_RESOURCE: Final[str]
CONF_RESOURCE_TEMPLATE: Final[str]
CONF_RESOURCES: Final[str]
CONF_RESPONSE_VARIABLE: Final[str]
CONF_RGB: Final[str]
CONF_ROOM: Final[str]
CONF_SCAN_INTERVAL: Final[str]
CONF_SCENE: Final[str]
CONF_SELECTOR: Final[str]
CONF_SENDER: Final[str]
CONF_SENSORS: Final[str]
CONF_SENSOR_TYPE: Final[str]
CONF_SEQUENCE: Final[str]
CONF_SERVICE: Final[str]
CONF_SERVICE_DATA: Final[str]
CONF_SERVICE_DATA_TEMPLATE: Final[str]
CONF_SERVICE_TEMPLATE: Final[str]
CONF_SHOW_ON_MAP: Final[str]
CONF_SLAVE: Final[str]
CONF_SOURCE: Final[str]
CONF_SSL: Final[str]
CONF_STATE: Final[str]
CONF_STATE_TEMPLATE: Final[str]
CONF_STOP: Final[str]
CONF_STRUCTURE: Final[str]
CONF_SWITCHES: Final[str]
CONF_TARGET: Final[str]
CONF_TEMPERATURE_UNIT: Final[str]
CONF_THEN: Final[str]
CONF_TIMEOUT: Final[str]
CONF_TIME_ZONE: Final[str]
CONF_TOKEN: Final[str]
CONF_TRIGGER_TIME: Final[str]
CONF_TTL: Final[str]
CONF_TYPE: Final[str]
CONF_UNIQUE_ID: Final[str]
CONF_UNIT_OF_MEASUREMENT: Final[str]
CONF_UNIT_SYSTEM: Final[str]
CONF_UNTIL: Final[str]
CONF_URL: Final[str]
CONF_USERNAME: Final[str]
CONF_UUID: Final[str]
CONF_VALUE_TEMPLATE: Final[str]
CONF_VARIABLES: Final[str]
CONF_VERIFY_SSL: Final[str]
CONF_WAIT_FOR_TRIGGER: Final[str]
CONF_WAIT_TEMPLATE: Final[str]
CONF_WEBHOOK_ID: Final[str]
CONF_WEEKDAY: Final[str]
CONF_WHILE: Final[str]
CONF_WHITELIST: Final[str]
CONF_ALLOWLIST_EXTERNAL_DIRS: Final[str]
LEGACY_CONF_WHITELIST_EXTERNAL_DIRS: Final[str]
CONF_XY: Final[str]
CONF_ZONE: Final[str]
EVENT_CALL_SERVICE: Final[str]
EVENT_COMPONENT_LOADED: Final[str]
EVENT_CORE_CONFIG_UPDATE: Final[str]
EVENT_HOMEASSISTANT_CLOSE: Final[str]
EVENT_HOMEASSISTANT_START: Final[str]
EVENT_HOMEASSISTANT_STARTED: Final[str]
EVENT_HOMEASSISTANT_STOP: Final[str]
EVENT_HOMEASSISTANT_FINAL_WRITE: Final[str]
EVENT_LOGBOOK_ENTRY: Final[str]
EVENT_SERVICE_REGISTERED: Final[str]
EVENT_SERVICE_REMOVED: Final[str]
EVENT_STATE_CHANGED: Final[str]
EVENT_THEMES_UPDATED: Final[str]
DEVICE_CLASS_AQI: Final[str]
DEVICE_CLASS_BATTERY: Final[str]
DEVICE_CLASS_CO: Final[str]
DEVICE_CLASS_CO2: Final[str]
DEVICE_CLASS_CURRENT: Final[str]
DEVICE_CLASS_DATE: Final[str]
DEVICE_CLASS_ENERGY: Final[str]
DEVICE_CLASS_FREQUENCY: Final[str]
DEVICE_CLASS_GAS: Final[str]
DEVICE_CLASS_HUMIDITY: Final[str]
DEVICE_CLASS_ILLUMINANCE: Final[str]
DEVICE_CLASS_MONETARY: Final[str]
DEVICE_CLASS_NITROGEN_DIOXIDE: str
DEVICE_CLASS_NITROGEN_MONOXIDE: str
DEVICE_CLASS_NITROUS_OXIDE: str
DEVICE_CLASS_OZONE: Final[str]
DEVICE_CLASS_PM1: Final[str]
DEVICE_CLASS_PM10: Final[str]
DEVICE_CLASS_PM25: Final[str]
DEVICE_CLASS_POWER_FACTOR: Final[str]
DEVICE_CLASS_POWER: Final[str]
DEVICE_CLASS_PRESSURE: Final[str]
DEVICE_CLASS_SIGNAL_STRENGTH: Final[str]
DEVICE_CLASS_SULPHUR_DIOXIDE: str
DEVICE_CLASS_TEMPERATURE: Final[str]
DEVICE_CLASS_TIMESTAMP: Final[str]
DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS: str
DEVICE_CLASS_VOLTAGE: Final[str]
STATE_ON: Final[str]
STATE_OFF: Final[str]
STATE_HOME: Final[str]
STATE_NOT_HOME: Final[str]
STATE_UNKNOWN: Final[str]
STATE_OPEN: Final[str]
STATE_OPENING: Final[str]
STATE_CLOSED: Final[str]
STATE_CLOSING: Final[str]
STATE_BUFFERING: Final[str]
STATE_PLAYING: Final[str]
STATE_PAUSED: Final[str]
STATE_IDLE: Final[str]
STATE_STANDBY: Final[str]
STATE_ALARM_DISARMED: Final[str]
STATE_ALARM_ARMED_HOME: Final[str]
STATE_ALARM_ARMED_AWAY: Final[str]
STATE_ALARM_ARMED_NIGHT: Final[str]
STATE_ALARM_ARMED_VACATION: Final[str]
STATE_ALARM_ARMED_CUSTOM_BYPASS: Final[str]
STATE_ALARM_PENDING: Final[str]
STATE_ALARM_ARMING: Final[str]
STATE_ALARM_DISARMING: Final[str]
STATE_ALARM_TRIGGERED: Final[str]
STATE_LOCKED: Final[str]
STATE_UNLOCKED: Final[str]
STATE_LOCKING: Final[str]
STATE_UNLOCKING: Final[str]
STATE_JAMMED: Final[str]
STATE_UNAVAILABLE: Final[str]
STATE_OK: Final[str]
STATE_PROBLEM: Final[str]
ATTR_ATTRIBUTION: Final[str]
ATTR_CREDENTIALS: Final[str]
ATTR_NOW: Final[str]
ATTR_DATE: Final[str]
ATTR_TIME: Final[str]
ATTR_SECONDS: Final[str]
ATTR_DOMAIN: Final[str]
ATTR_SERVICE: Final[str]
ATTR_SERVICE_DATA: Final[str]
ATTR_ID: Final[str]
ATTR_NAME: Final[str]
ATTR_ENTITY_ID: Final[str]
ATTR_AREA_ID: Final[str]
ATTR_DEVICE_ID: Final[str]
ATTR_FRIENDLY_NAME: Final[str]
ATTR_ENTITY_PICTURE: Final[str]
ATTR_IDENTIFIERS: Final[str]
ATTR_ICON: Final[str]
ATTR_UNIT_OF_MEASUREMENT: Final[str]
CONF_UNIT_SYSTEM_METRIC: Final[str]
CONF_UNIT_SYSTEM_IMPERIAL: Final[str]
ATTR_VOLTAGE: Final[str]
ATTR_LOCATION: Final[str]
ATTR_MODE: Final[str]
ATTR_CONFIGURATION_URL: Final[str]
ATTR_CONNECTIONS: Final[str]
ATTR_DEFAULT_NAME: Final[str]
ATTR_MANUFACTURER: Final[str]
ATTR_MODEL: Final[str]
ATTR_SUGGESTED_AREA: Final[str]
ATTR_SW_VERSION: Final[str]
ATTR_HW_VERSION: Final[str]
ATTR_VIA_DEVICE: Final[str]
ATTR_BATTERY_CHARGING: Final[str]
ATTR_BATTERY_LEVEL: Final[str]
ATTR_WAKEUP: Final[str]
ATTR_CODE: Final[str]
ATTR_CODE_FORMAT: Final[str]
ATTR_COMMAND: Final[str]
ATTR_ARMED: Final[str]
ATTR_LOCKED: Final[str]
ATTR_TRIPPED: Final[str]
ATTR_LAST_TRIP_TIME: Final[str]
ATTR_HIDDEN: Final[str]
ATTR_LATITUDE: Final[str]
ATTR_LONGITUDE: Final[str]
ATTR_GPS_ACCURACY: Final[str]
ATTR_ASSUMED_STATE: Final[str]
ATTR_STATE: Final[str]
ATTR_EDITABLE: Final[str]
ATTR_OPTION: Final[str]
ATTR_RESTORED: Final[str]
ATTR_SUPPORTED_FEATURES: Final[str]
ATTR_DEVICE_CLASS: Final[str]
ATTR_TEMPERATURE: Final[str]
ATTR_PERSONS: Final[str]

class UnitOfApparentPower(StrEnum):
    VOLT_AMPERE: str

POWER_VOLT_AMPERE: Final[str]

class UnitOfPower(StrEnum):
    WATT: str
    KILO_WATT: str
    BTU_PER_HOUR: str

POWER_WATT: Final[str]
POWER_KILO_WATT: Final[str]
POWER_BTU_PER_HOUR: Final[str]
POWER_VOLT_AMPERE_REACTIVE: Final[str]

class UnitOfEnergy(StrEnum):
    GIGA_JOULE: str
    KILO_WATT_HOUR: str
    MEGA_JOULE: str
    MEGA_WATT_HOUR: str
    WATT_HOUR: str

ENERGY_KILO_WATT_HOUR: Final[str]
ENERGY_MEGA_WATT_HOUR: Final[str]
ENERGY_WATT_HOUR: Final[str]

class UnitOfElectricCurrent(StrEnum):
    MILLIAMPERE: str
    AMPERE: str

ELECTRIC_CURRENT_MILLIAMPERE: Final[str]
ELECTRIC_CURRENT_AMPERE: Final[str]

class UnitOfElectricPotential(StrEnum):
    MILLIVOLT: str
    VOLT: str

ELECTRIC_POTENTIAL_MILLIVOLT: Final[str]
ELECTRIC_POTENTIAL_VOLT: Final[str]
DEGREE: Final[str]
CURRENCY_EURO: Final[str]
CURRENCY_DOLLAR: Final[str]
CURRENCY_CENT: Final[str]

class UnitOfTemperature(StrEnum):
    CELSIUS: str
    FAHRENHEIT: str
    KELVIN: str

TEMP_CELSIUS: Final[str]
TEMP_FAHRENHEIT: Final[str]
TEMP_KELVIN: Final[str]

class UnitOfTime(StrEnum):
    MICROSECONDS: str
    MILLISECONDS: str
    SECONDS: str
    MINUTES: str
    HOURS: str
    DAYS: str
    WEEKS: str
    MONTHS: str
    YEARS: str

TIME_MICROSECONDS: Final[str]
TIME_MILLISECONDS: Final[str]
TIME_SECONDS: Final[str]
TIME_MINUTES: Final[str]
TIME_HOURS: Final[str]
TIME_DAYS: Final[str]
TIME_WEEKS: Final[str]
TIME_MONTHS: Final[str]
TIME_YEARS: Final[str]

class UnitOfLength(StrEnum):
    MILLIMETERS: str
    CENTIMETERS: str
    METERS: str
    KILOMETERS: str
    INCHES: str
    FEET: str
    YARDS: str
    MILES: str

LENGTH_MILLIMETERS: Final[str]
LENGTH_CENTIMETERS: Final[str]
LENGTH_METERS: Final[str]
LENGTH_KILOMETERS: Final[str]
LENGTH_INCHES: Final[str]
LENGTH_FEET: Final[str]
LENGTH_YARD: Final[str]
LENGTH_MILES: Final[str]

class UnitOfFrequency(StrEnum):
    HERTZ: str
    KILOHERTZ: str
    MEGAHERTZ: str
    GIGAHERTZ: str

FREQUENCY_HERTZ: Final[str]
FREQUENCY_KILOHERTZ: Final[str]
FREQUENCY_MEGAHERTZ: Final[str]
FREQUENCY_GIGAHERTZ: Final[str]

class UnitOfPressure(StrEnum):
    PA: str
    HPA: str
    KPA: str
    BAR: str
    CBAR: str
    MBAR: str
    MMHG: str
    INHG: str
    PSI: str

PRESSURE_PA: Final[str]
PRESSURE_HPA: Final[str]
PRESSURE_KPA: Final[str]
PRESSURE_BAR: Final[str]
PRESSURE_CBAR: Final[str]
PRESSURE_MBAR: Final[str]
PRESSURE_MMHG: Final[str]
PRESSURE_INHG: Final[str]
PRESSURE_PSI: Final[str]

class UnitOfSoundPressure(StrEnum):
    DECIBEL: str
    WEIGHTED_DECIBEL_A: str

SOUND_PRESSURE_DB: Final[str]
SOUND_PRESSURE_WEIGHTED_DBA: Final[str]

class UnitOfVolume(StrEnum):
    CUBIC_FEET: str
    CENTUM_CUBIC_FEET: str
    CUBIC_METERS: str
    LITERS: str
    MILLILITERS: str
    GALLONS: str
    FLUID_OUNCES: str

VOLUME_LITERS: Final[str]
VOLUME_MILLILITERS: Final[str]
VOLUME_CUBIC_METERS: Final[str]
VOLUME_CUBIC_FEET: Final[str]
VOLUME_GALLONS: Final[str]
VOLUME_FLUID_OUNCE: Final[str]

class UnitOfVolumeFlowRate(StrEnum):
    CUBIC_METERS_PER_HOUR: str
    CUBIC_FEET_PER_MINUTE: str

VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR: Final[str]
VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE: Final[str]
AREA_SQUARE_METERS: Final[str]

class UnitOfMass(StrEnum):
    GRAMS: str
    KILOGRAMS: str
    MILLIGRAMS: str
    MICROGRAMS: str
    OUNCES: str
    POUNDS: str
    STONES: str

MASS_GRAMS: Final[str]
MASS_KILOGRAMS: Final[str]
MASS_MILLIGRAMS: Final[str]
MASS_MICROGRAMS: Final[str]
MASS_OUNCES: Final[str]
MASS_POUNDS: Final[str]
CONDUCTIVITY: Final[str]
LIGHT_LUX: Final[str]
UV_INDEX: Final[str]
PERCENTAGE: Final[str]
REVOLUTIONS_PER_MINUTE: Final[str]

class UnitOfIrradiance(StrEnum):
    WATTS_PER_SQUARE_METER: str
    BTUS_PER_HOUR_SQUARE_FOOT: str

IRRADIATION_WATTS_PER_SQUARE_METER: Final[str]
IRRADIATION_BTUS_PER_HOUR_SQUARE_FOOT: Final[str]

class UnitOfVolumetricFlux(StrEnum):
    INCHES_PER_DAY: str
    INCHES_PER_HOUR: str
    MILLIMETERS_PER_DAY: str
    MILLIMETERS_PER_HOUR: str

class UnitOfPrecipitationDepth(StrEnum):
    INCHES: str
    MILLIMETERS: str
    CENTIMETERS: str

PRECIPITATION_INCHES: Final[str]
PRECIPITATION_MILLIMETERS: Final[str]
PRECIPITATION_MILLIMETERS_PER_HOUR: Final[str]
PRECIPITATION_INCHES_PER_HOUR: Final[str]
CONCENTRATION_MICROGRAMS_PER_CUBIC_METER: Final[str]
CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER: Final[str]
CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT: Final[str]
CONCENTRATION_PARTS_PER_CUBIC_METER: Final[str]
CONCENTRATION_PARTS_PER_MILLION: Final[str]
CONCENTRATION_PARTS_PER_BILLION: Final[str]

class UnitOfSpeed(StrEnum):
    FEET_PER_SECOND: str
    METERS_PER_SECOND: str
    KILOMETERS_PER_HOUR: str
    KNOTS: str
    MILES_PER_HOUR: str

SPEED_FEET_PER_SECOND: Final[str]
SPEED_METERS_PER_SECOND: Final[str]
SPEED_KILOMETERS_PER_HOUR: Final[str]
SPEED_KNOTS: Final[str]
SPEED_MILES_PER_HOUR: Final[str]
SPEED_MILLIMETERS_PER_DAY: Final[str]
SPEED_INCHES_PER_DAY: Final[str]
SPEED_INCHES_PER_HOUR: Final[str]
SIGNAL_STRENGTH_DECIBELS: Final[str]
SIGNAL_STRENGTH_DECIBELS_MILLIWATT: Final[str]

class UnitOfInformation(StrEnum):
    BITS: str
    KILOBITS: str
    MEGABITS: str
    GIGABITS: str
    BYTES: str
    KILOBYTES: str
    MEGABYTES: str
    GIGABYTES: str
    TERABYTES: str
    PETABYTES: str
    EXABYTES: str
    ZETTABYTES: str
    YOTTABYTES: str
    KIBIBYTES: str
    MEBIBYTES: str
    GIBIBYTES: str
    TEBIBYTES: str
    PEBIBYTES: str
    EXBIBYTES: str
    ZEBIBYTES: str
    YOBIBYTES: str

DATA_BITS: Final[str]
DATA_KILOBITS: Final[str]
DATA_MEGABITS: Final[str]
DATA_GIGABITS: Final[str]
DATA_BYTES: Final[str]
DATA_KILOBYTES: Final[str]
DATA_MEGABYTES: Final[str]
DATA_GIGABYTES: Final[str]
DATA_TERABYTES: Final[str]
DATA_PETABYTES: Final[str]
DATA_EXABYTES: Final[str]
DATA_ZETTABYTES: Final[str]
DATA_YOTTABYTES: Final[str]
DATA_KIBIBYTES: Final[str]
DATA_MEBIBYTES: Final[str]
DATA_GIBIBYTES: Final[str]
DATA_TEBIBYTES: Final[str]
DATA_PEBIBYTES: Final[str]
DATA_EXBIBYTES: Final[str]
DATA_ZEBIBYTES: Final[str]
DATA_YOBIBYTES: Final[str]

class UnitOfDataRate(StrEnum):
    BITS_PER_SECOND: str
    KILOBITS_PER_SECOND: str
    MEGABITS_PER_SECOND: str
    GIGABITS_PER_SECOND: str
    BYTES_PER_SECOND: str
    KILOBYTES_PER_SECOND: str
    MEGABYTES_PER_SECOND: str
    GIGABYTES_PER_SECOND: str
    KIBIBYTES_PER_SECOND: str
    MEBIBYTES_PER_SECOND: str
    GIBIBYTES_PER_SECOND: str

DATA_RATE_BITS_PER_SECOND: Final[str]
DATA_RATE_KILOBITS_PER_SECOND: Final[str]
DATA_RATE_MEGABITS_PER_SECOND: Final[str]
DATA_RATE_GIGABITS_PER_SECOND: Final[str]
DATA_RATE_BYTES_PER_SECOND: Final[str]
DATA_RATE_KILOBYTES_PER_SECOND: Final[str]
DATA_RATE_MEGABYTES_PER_SECOND: Final[str]
DATA_RATE_GIGABYTES_PER_SECOND: Final[str]
DATA_RATE_KIBIBYTES_PER_SECOND: Final[str]
DATA_RATE_MEBIBYTES_PER_SECOND: Final[str]
DATA_RATE_GIBIBYTES_PER_SECOND: Final[str]
COMPRESSED_STATE_STATE: str
COMPRESSED_STATE_ATTRIBUTES: str
COMPRESSED_STATE_CONTEXT: str
COMPRESSED_STATE_LAST_CHANGED: str
COMPRESSED_STATE_LAST_UPDATED: str
SERVICE_HOMEASSISTANT_STOP: Final[str]
SERVICE_HOMEASSISTANT_RESTART: Final[str]
SERVICE_TURN_ON: Final[str]
SERVICE_TURN_OFF: Final[str]
SERVICE_TOGGLE: Final[str]
SERVICE_RELOAD: Final[str]
SERVICE_VOLUME_UP: Final[str]
SERVICE_VOLUME_DOWN: Final[str]
SERVICE_VOLUME_MUTE: Final[str]
SERVICE_VOLUME_SET: Final[str]
SERVICE_MEDIA_PLAY_PAUSE: Final[str]
SERVICE_MEDIA_PLAY: Final[str]
SERVICE_MEDIA_PAUSE: Final[str]
SERVICE_MEDIA_STOP: Final[str]
SERVICE_MEDIA_NEXT_TRACK: Final[str]
SERVICE_MEDIA_PREVIOUS_TRACK: Final[str]
SERVICE_MEDIA_SEEK: Final[str]
SERVICE_REPEAT_SET: Final[str]
SERVICE_SHUFFLE_SET: Final[str]
SERVICE_ALARM_DISARM: Final[str]
SERVICE_ALARM_ARM_HOME: Final[str]
SERVICE_ALARM_ARM_AWAY: Final[str]
SERVICE_ALARM_ARM_NIGHT: Final[str]
SERVICE_ALARM_ARM_VACATION: Final[str]
SERVICE_ALARM_ARM_CUSTOM_BYPASS: Final[str]
SERVICE_ALARM_TRIGGER: Final[str]
SERVICE_LOCK: Final[str]
SERVICE_UNLOCK: Final[str]
SERVICE_OPEN: Final[str]
SERVICE_CLOSE: Final[str]
SERVICE_CLOSE_COVER: Final[str]
SERVICE_CLOSE_COVER_TILT: Final[str]
SERVICE_OPEN_COVER: Final[str]
SERVICE_OPEN_COVER_TILT: Final[str]
SERVICE_SAVE_PERSISTENT_STATES: Final[str]
SERVICE_SET_COVER_POSITION: Final[str]
SERVICE_SET_COVER_TILT_POSITION: Final[str]
SERVICE_STOP_COVER: Final[str]
SERVICE_STOP_COVER_TILT: Final[str]
SERVICE_TOGGLE_COVER_TILT: Final[str]
SERVICE_SELECT_OPTION: Final[str]
SERVER_PORT: Final[int]
URL_ROOT: Final[str]
URL_API: Final[str]
URL_API_STREAM: Final[str]
URL_API_CORE_STATE: Final[str]
URL_API_CONFIG: Final[str]
URL_API_STATES: Final[str]
URL_API_STATES_ENTITY: Final[str]
URL_API_EVENTS: Final[str]
URL_API_EVENTS_EVENT: Final[str]
URL_API_SERVICES: Final[str]
URL_API_SERVICES_SERVICE: Final[str]
URL_API_COMPONENTS: Final[str]
URL_API_ERROR_LOG: Final[str]
URL_API_LOG_OUT: Final[str]
URL_API_TEMPLATE: Final[str]
HTTP_BASIC_AUTHENTICATION: Final[str]
HTTP_BEARER_AUTHENTICATION: Final[str]
HTTP_DIGEST_AUTHENTICATION: Final[str]
HTTP_HEADER_X_REQUESTED_WITH: Final[str]
CONTENT_TYPE_JSON: Final[str]
CONTENT_TYPE_MULTIPART: Final[str]
CONTENT_TYPE_TEXT_PLAIN: Final[str]
RESTART_EXIT_CODE: Final[int]
UNIT_NOT_RECOGNIZED_TEMPLATE: Final[str]
LENGTH: Final[str]
MASS: Final[str]
PRESSURE: Final[str]
VOLUME: Final[str]
TEMPERATURE: Final[str]
SPEED: Final[str]
WIND_SPEED: Final[str]
ILLUMINANCE: Final[str]
ACCUMULATED_PRECIPITATION: Final[str]
WEEKDAYS: Final[list[str]]
PRECISION_WHOLE: Final[int]
PRECISION_HALVES: Final[float]
PRECISION_TENTHS: Final[float]
CLOUD_NEVER_EXPOSED_ENTITIES: Final[list[str]]
ENTITY_CATEGORY_CONFIG: Final[str]
ENTITY_CATEGORY_DIAGNOSTIC: Final[str]
ENTITY_CATEGORIES: Final[list[str]]
CAST_APP_ID_HOMEASSISTANT_MEDIA: Final[str]
CAST_APP_ID_HOMEASSISTANT_LOVELACE: Final[str]
HASSIO_USER_NAME: str
SIGNAL_BOOTSTRAP_INTEGRATIONS: str
FORMAT_DATE: Final[str]
FORMAT_TIME: Final[str]
FORMAT_DATETIME: Final[Incomplete]

class EntityCategory(StrEnum):
    CONFIG: str
    DIAGNOSTIC: str
