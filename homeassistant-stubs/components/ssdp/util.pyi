from defusedxml import ElementTree as ElementTree
from typing import Any

def etree_to_dict(tree: ElementTree) -> dict[str, Union[dict[str, Any], None]]: ...
