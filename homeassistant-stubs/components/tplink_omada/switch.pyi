from .const import DOMAIN as DOMAIN
from .coordinator import OmadaCoordinator as OmadaCoordinator
from .entity import OmadaSwitchDeviceEntity as OmadaSwitchDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tplink_omada_client.devices import OmadaSwitch as OmadaSwitch, OmadaSwitchPortDetails
from tplink_omada_client.omadasiteclient import OmadaSiteClient as OmadaSiteClient
from typing import Any

POE_SWITCH_ICON: str

async def poll_switch_state(client: OmadaSiteClient, network_switch: OmadaSwitch) -> dict[str, OmadaSwitchPortDetails]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_port_base_name(port: OmadaSwitchPortDetails) -> str: ...

class OmadaNetworkSwitchPortPoEControl(OmadaSwitchDeviceEntity, SwitchEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    _attr_icon: Incomplete
    port_id: Incomplete
    port_details: Incomplete
    omada_client: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: OmadaCoordinator[OmadaSwitchPortDetails], device: OmadaSwitch, port_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _async_turn_on_off_poe(self, enable: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    def _refresh_state(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
