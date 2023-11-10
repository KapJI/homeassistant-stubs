from .coordinator import JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from dataclasses import dataclass
from jellyfin_apiclient_python import JellyfinClient as JellyfinClient

@dataclass
class JellyfinData:
    client_device_id: str
    jellyfin_client: JellyfinClient
    coordinators: dict[str, JellyfinDataUpdateCoordinator]
    def __init__(self, client_device_id, jellyfin_client, coordinators) -> None: ...
