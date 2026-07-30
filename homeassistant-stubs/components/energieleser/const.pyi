from _typeshed import Incomplete
from energieleser import DeviceType
from typing import Final

DOMAIN: Final[str]
LOGGER: Incomplete
CONF_SW_VERSION: Final[str]
DEVICE_MODEL_NAMES: dict[DeviceType, str]

def device_model_name(device_type: DeviceType) -> str: ...
