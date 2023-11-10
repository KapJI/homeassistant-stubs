from .utils import BondHub as BondHub
from bond_async import BPUPSubscriptions as BPUPSubscriptions
from dataclasses import dataclass

@dataclass
class BondData:
    hub: BondHub
    bpup_subs: BPUPSubscriptions
    def __init__(self, hub, bpup_subs) -> None: ...
