from enum import StrEnum

DOMAIN: str

class SelectEntityCapabilityAttribute(StrEnum):
    OPTIONS = 'options'

ATTR_CYCLE: str
ATTR_OPTIONS: str
CONF_CYCLE: str
CONF_OPTION: str
SERVICE_SELECT_FIRST: str
SERVICE_SELECT_LAST: str
SERVICE_SELECT_NEXT: str
SERVICE_SELECT_PREVIOUS: str
