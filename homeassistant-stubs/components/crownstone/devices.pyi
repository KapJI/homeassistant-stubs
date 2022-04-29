from .const import CROWNSTONE_INCLUDE_TYPES as CROWNSTONE_INCLUDE_TYPES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from crownstone_cloud.cloud_models.crownstones import Crownstone as Crownstone
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity

class CrownstoneBaseEntity(Entity):
    _attr_should_poll: bool
    device: Incomplete
    def __init__(self, device: Crownstone) -> None: ...
    @property
    def cloud_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
