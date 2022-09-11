from .models import HaBleakClientWrapper as HaBleakClientWrapper, HaBleakScannerWrapper as HaBleakScannerWrapper
from _typeshed import Incomplete

ORIGINAL_BLEAK_SCANNER: Incomplete
ORIGINAL_BLEAK_CLIENT: Incomplete

def install_multiple_bleak_catcher() -> None: ...
def uninstall_multiple_bleak_catcher() -> None: ...
