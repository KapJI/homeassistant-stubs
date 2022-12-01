from .wrappers import HaBleakClientWrapper as HaBleakClientWrapper, HaBleakScannerWrapper as HaBleakScannerWrapper
from _typeshed import Incomplete
from bleak.backends.service import BleakGATTServiceCollection as BleakGATTServiceCollection

ORIGINAL_BLEAK_SCANNER: Incomplete
ORIGINAL_BLEAK_CLIENT: Incomplete
ORIGINAL_BLEAK_RETRY_CONNECTOR_CLIENT: Incomplete

def install_multiple_bleak_catcher() -> None: ...
def uninstall_multiple_bleak_catcher() -> None: ...

class HaBleakClientWithServiceCache(HaBleakClientWrapper):
    def set_cached_services(self, services: Union[BleakGATTServiceCollection, None]) -> None: ...
