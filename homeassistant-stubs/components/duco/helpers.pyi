from .const import BOX_NODE_ID as BOX_NODE_ID
from .coordinator import DucoCoordinator as DucoCoordinator
from homeassistant.core import callback as callback

@callback
def remove_stale_node_ids(coordinator: DucoCoordinator, known_nodes: set[int]) -> None: ...
