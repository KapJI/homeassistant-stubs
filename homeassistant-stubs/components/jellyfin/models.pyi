from .coordinator import JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from jellyfin_apiclient_python import JellyfinClient as JellyfinClient

class JellyfinData:
    client_device_id: str
    jellyfin_client: JellyfinClient
    coordinators: dict[str, JellyfinDataUpdateCoordinator]
    def __init__(self, client_device_id, jellyfin_client, coordinators) -> None: ...
