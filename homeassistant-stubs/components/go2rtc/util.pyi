from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera
from pathlib import Path

_HA_MANAGED_UNIX_SOCKET_FILE: str
_SAFE_CHARS: Incomplete

def get_go2rtc_unix_socket_path(path: str | Path) -> str: ...
def get_camera_identifier(camera: Camera) -> str: ...
