from ..const import CONF_SCHEMA as CONF_SCHEMA
from _typeshed import Incomplete
from homeassistant.components.vacuum import VacuumEntityFeature as VacuumEntityFeature

LEGACY: str
STATE: str
MQTT_VACUUM_SCHEMA: Incomplete

def services_to_strings(services: VacuumEntityFeature, service_to_string: dict[VacuumEntityFeature, str]) -> list[str]: ...
def strings_to_services(strings: list[str], string_to_service: dict[str, VacuumEntityFeature]) -> VacuumEntityFeature: ...
