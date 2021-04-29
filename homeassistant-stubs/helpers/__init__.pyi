from .typing import ConfigType as ConfigType
from collections.abc import Iterable, Sequence
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM
from typing import Any

def config_per_platform(config: ConfigType, domain: str) -> Iterable[tuple[Any, Any]]: ...
def extract_domain_configs(config: ConfigType, domain: str) -> Sequence[str]: ...
