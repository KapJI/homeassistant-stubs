from homeassistant.helpers.device_registry import format_mac as format_mac
from huawei_lte_api.Session import GetResponseType as GetResponseType

def get_device_macs(device_info: GetResponseType, wlan_settings: GetResponseType) -> list[str]: ...
