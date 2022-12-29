from homeassistant.backports.enum import StrEnum as StrEnum

DOMAIN: str
REDACTED: str

class DiagnosticsType(StrEnum):
    CONFIG_ENTRY: str

class DiagnosticsSubType(StrEnum):
    DEVICE: str
