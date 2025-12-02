from _typeshed import Incomplete
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class DefaultArea:
    key: str
    icon: str

DOMAIN: str
STEP_USER: str
STEP_CORE_CONFIG: str
STEP_INTEGRATION: str
STEP_ANALYTICS: str
STEPS: Incomplete
DEFAULT_AREAS: Incomplete
