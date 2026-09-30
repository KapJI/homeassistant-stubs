from . import UpdateEntity as UpdateEntity
from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[UpdateEntity]]

class UpdateEntityStateAttribute(StrEnum):
    AUTO_UPDATE = 'auto_update'
    DISPLAY_PRECISION = 'display_precision'
    INSTALLED_VERSION = 'installed_version'
    IN_PROGRESS = 'in_progress'
    LATEST_VERSION = 'latest_version'
    RELEASE_SUMMARY = 'release_summary'
    RELEASE_URL = 'release_url'
    SKIPPED_VERSION = 'skipped_version'
    TITLE = 'title'
    UPDATE_PERCENTAGE = 'update_percentage'

class UpdateEntityFeature(IntFlag):
    INSTALL = 1
    SPECIFIC_VERSION = 2
    PROGRESS = 4
    BACKUP = 8
    RELEASE_NOTES = 16

SERVICE_INSTALL: Final[str]
SERVICE_SKIP: Final[str]
ATTR_AUTO_UPDATE: Final[str]
ATTR_BACKUP: Final[str]
ATTR_DISPLAY_PRECISION: Final[str]
ATTR_INSTALLED_VERSION: Final[str]
ATTR_IN_PROGRESS: Final[str]
ATTR_LATEST_VERSION: Final[str]
ATTR_RELEASE_SUMMARY: Final[str]
ATTR_RELEASE_URL: Final[str]
ATTR_SKIPPED_VERSION: Final[str]
ATTR_TITLE: Final[str]
ATTR_UPDATE_PERCENTAGE: Final[str]
ATTR_VERSION: Final[str]

class UpdateDeviceClass(StrEnum):
    FIRMWARE = 'firmware'

DEVICE_CLASSES_SCHEMA: Incomplete
