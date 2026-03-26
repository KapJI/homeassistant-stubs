from enum import IntEnum, StrEnum

DOMAIN: str
DEFAULT_NAME: str
API_MAX_RETRIES: int

class EndpointStatus(IntEnum):
    UP = 1
    DOWN = 2

class ContainerState(StrEnum):
    RUNNING = 'running'

class StackStatus(IntEnum):
    ACTIVE = 1
    INACTIVE = 2

class StackType(IntEnum):
    SWARM = 1
    COMPOSE = 2
    KUBERNETES = 3
