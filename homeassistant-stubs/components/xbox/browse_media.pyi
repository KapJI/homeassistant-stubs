from .entity import to_https as to_https
from _typeshed import Incomplete
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaClass as MediaClass, MediaType as MediaType
from pythonxbox.api.client import XboxLiveClient as XboxLiveClient
from pythonxbox.api.provider.catalog.models import CatalogResponse as CatalogResponse, Image as Image
from pythonxbox.api.provider.smartglass.models import InstalledPackage as InstalledPackage, InstalledPackagesList as InstalledPackagesList
from typing import NamedTuple

class MediaTypeDetails(NamedTuple):
    type: str
    cls: str

TYPE_MAP: Incomplete

async def build_item_response(client: XboxLiveClient, device_id: str, media_content_type: MediaType | str | None = None, media_content_id: str | None = None) -> BrowseMedia: ...
def item_payload(item: InstalledPackage, images: dict[str, list[Image]]) -> BrowseMedia: ...
def _find_media_image(images: list[Image]) -> str | None: ...
