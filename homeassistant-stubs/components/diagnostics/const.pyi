from enum import StrEnum

DOMAIN: str
REDACTED: str

class DiagnosticsType(StrEnum):
    CONFIG_ENTRY: str

class DiagnosticsSubType(StrEnum):
    DEVICE: str
