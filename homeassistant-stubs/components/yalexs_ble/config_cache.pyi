from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.hass_dict import HassKey as HassKey
from yalexs_ble import ValidatedLockConfig as ValidatedLockConfig

CONFIG_CACHE: HassKey[dict[str, ValidatedLockConfig]]

@callback
def async_add_validated_config(hass: HomeAssistant, address: str, config: ValidatedLockConfig) -> None: ...
@callback
def async_get_validated_config(hass: HomeAssistant, address: str) -> ValidatedLockConfig | None: ...
