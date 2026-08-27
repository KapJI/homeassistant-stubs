from enum import StrEnum

DOMAIN: str

class FlowType(StrEnum):
    CONFIG_FLOW = 'config_flow'
    OPTIONS_FLOW = 'options_flow'
    CONFIG_SUBENTRIES_FLOW = 'config_subentries_flow'
