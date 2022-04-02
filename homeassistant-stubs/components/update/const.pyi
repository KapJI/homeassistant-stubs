from enum import IntEnum
from typing import Final

DOMAIN: Final[str]

class UpdateEntityFeature(IntEnum):
    INSTALL: int
    SPECIFIC_VERSION: int
    PROGRESS: int
    BACKUP: int
    RELEASE_NOTES: int

SERVICE_INSTALL: Final[str]
SERVICE_SKIP: Final[str]
ATTR_AUTO_UPDATE: Final[str]
ATTR_BACKUP: Final[str]
ATTR_INSTALLED_VERSION: Final[str]
ATTR_IN_PROGRESS: Final[str]
ATTR_LATEST_VERSION: Final[str]
ATTR_RELEASE_SUMMARY: Final[str]
ATTR_RELEASE_URL: Final[str]
ATTR_SKIPPED_VERSION: Final[str]
ATTR_TITLE: Final[str]
ATTR_VERSION: Final[str]
