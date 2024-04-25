from .models import Eq3Config as Eq3Config
from _typeshed import Incomplete
from eq3btsmart.thermostat import Thermostat as Thermostat
from homeassistant.helpers.entity import Entity as Entity

class Eq3Entity(Entity):
    _attr_has_entity_name: bool
    _eq3_config: Incomplete
    _thermostat: Incomplete
    def __init__(self, eq3_config: Eq3Config, thermostat: Thermostat) -> None: ...
