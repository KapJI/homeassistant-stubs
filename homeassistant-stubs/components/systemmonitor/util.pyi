from .const import CPU_SENSOR_PREFIXES as CPU_SENSOR_PREFIXES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from psutil._common import shwtemp as shwtemp

_LOGGER: Incomplete
SKIP_DISK_TYPES: Incomplete

def get_all_disk_mounts(hass: HomeAssistant) -> set[str]: ...
def get_all_network_interfaces(hass: HomeAssistant) -> set[str]: ...
def get_all_running_processes(hass: HomeAssistant) -> set[str]: ...
def read_cpu_temperature(hass: HomeAssistant, temps: dict[str, list[shwtemp]] | None = None) -> float | None: ...
