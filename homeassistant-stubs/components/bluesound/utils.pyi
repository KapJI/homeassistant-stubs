from homeassistant.helpers.device_registry import format_mac as format_mac

def format_unique_id(mac: str, port: int) -> str: ...
def dispatcher_join_signal(entity_id: str) -> str: ...
def dispatcher_unjoin_signal(leader_id: str) -> str: ...
