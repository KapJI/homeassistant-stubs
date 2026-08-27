from dataclasses import dataclass, field
from wiim.controller import WiimController as WiimController

@dataclass
class WiimData:
    controller: WiimController
    entity_id_to_udn_map: dict[str, str] = field(default_factory=dict)
