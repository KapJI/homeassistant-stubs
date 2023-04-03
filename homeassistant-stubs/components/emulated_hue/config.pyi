from _typeshed import Incomplete
from homeassistant.components import climate as climate, cover as cover, fan as fan, humidifier as humidifier, light as light, media_player as media_player, scene as scene, script as script
from homeassistant.const import CONF_ENTITIES as CONF_ENTITIES, CONF_TYPE as CONF_TYPE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers import storage as storage
from homeassistant.helpers.event import async_track_state_added_domain as async_track_state_added_domain, async_track_state_removed_domain as async_track_state_removed_domain
from homeassistant.helpers.typing import ConfigType as ConfigType

SUPPORTED_DOMAINS: Incomplete
TYPE_ALEXA: str
TYPE_GOOGLE: str
NUMBERS_FILE: str
DATA_KEY: str
DATA_VERSION: str
SAVE_DELAY: int
CONF_ADVERTISE_IP: str
CONF_ADVERTISE_PORT: str
CONF_ENTITY_HIDDEN: str
CONF_ENTITY_NAME: str
CONF_EXPOSE_BY_DEFAULT: str
CONF_EXPOSED_DOMAINS: str
CONF_HOST_IP: str
CONF_LIGHTS_ALL_DIMMABLE: str
CONF_LISTEN_PORT: str
CONF_OFF_MAPS_TO_ON_DOMAINS: str
CONF_UPNP_BIND_MULTICAST: str
DEFAULT_LIGHTS_ALL_DIMMABLE: bool
DEFAULT_LISTEN_PORT: int
DEFAULT_UPNP_BIND_MULTICAST: bool
DEFAULT_OFF_MAPS_TO_ON_DOMAINS: Incomplete
DEFAULT_EXPOSE_BY_DEFAULT: bool
DEFAULT_EXPOSED_DOMAINS: Incomplete
DEFAULT_TYPE = TYPE_GOOGLE
ATTR_EMULATED_HUE_NAME: str
_LOGGER: Incomplete

class Config:
    hass: Incomplete
    type: Incomplete
    numbers: Incomplete
    store: Incomplete
    cached_states: Incomplete
    _exposed_cache: Incomplete
    host_ip_addr: Incomplete
    listen_port: Incomplete
    upnp_bind_multicast: Incomplete
    off_maps_to_on_domains: Incomplete
    expose_by_default: Incomplete
    exposed_domains: Incomplete
    advertise_ip: Incomplete
    advertise_port: Incomplete
    entities: Incomplete
    _entities_with_hidden_attr_in_config: Incomplete
    lights_all_dimmable: Incomplete
    track_domains: Incomplete
    def __init__(self, hass: HomeAssistant, conf: ConfigType, local_ip: str) -> None: ...
    async def async_setup(self) -> None: ...
    def entity_id_to_number(self, entity_id: str) -> str: ...
    def number_to_entity_id(self, number: str) -> str | None: ...
    def get_entity_name(self, state: State) -> str: ...
    def get_exposed_states(self) -> list[State]: ...
    def _clear_exposed_cache(self, event: Event) -> None: ...
    def is_state_exposed(self, state: State) -> bool: ...
    def _is_state_exposed(self, state: State) -> bool: ...
