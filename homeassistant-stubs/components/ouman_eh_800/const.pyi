from enum import StrEnum

DOMAIN: str
DEFAULT_SCAN_INTERVAL_SECONDS: int

class OumanDevice(StrEnum):
    MAIN = 'main'
    L1 = 'l1'
    L2 = 'l2'
